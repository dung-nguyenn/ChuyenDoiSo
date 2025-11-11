import streamlit as st
import os
from pydantic import BaseModel, Field
from typing import Type

# Thư viện LangChain
from langchain.agents import initialize_agent, AgentType
from langchain_core.tools import tool
# Import cho Gemini (API miễn phí/Free Tier)
from langchain_google_genai import ChatGoogleGenerativeAI 

# --- THÊM THƯ VIỆN DATABASE ---
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# --- 1. MÔ PHỎNG VÀ DATABASE SETUP ---

# --- THIẾT LẬP DATABASE (SQLITE) ---
DATABASE_URL = "sqlite:///spa_appointments.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Định nghĩa Model (Bảng) cho Lịch hẹn
class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    service_name = Column(String)
    date_time = Column(String, unique=True) # Đảm bảo không trùng lịch
    price = Column(String)
    duration = Column(String)

# Khởi tạo Database (Chỉ chạy 1 lần)
# Lệnh này sẽ tạo file spa_appointments.db nếu nó chưa tồn tại
Base.metadata.create_all(bind=engine)

# Tạo Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Hàm tiện ích để lấy lịch hẹn từ DB
def get_appointments_from_db():
    db = SessionLocal()
    try:
        # Lấy tất cả các bản ghi từ bảng appointments
        appointments = db.query(Appointment).all()
        # Chuyển đổi thành dictionary list để Streamlit hiển thị
        return [{
            "customer_name": appt.customer_name,
            "service_name": appt.service_name,
            "date_time": appt.date_time,
            "details": {"price": appt.price, "duration": appt.duration}
        } for appt in appointments]
    finally:
        db.close()


# Khởi tạo danh sách lịch hẹn trong session state (Đọc từ DB khi khởi chạy)
if 'SCHEDULED_APPOINTMENTS' not in st.session_state:
    st.session_state.SCHEDULED_APPOINTMENTS = get_appointments_from_db()


AVAILABLE_SERVICES = {
    "Massage Body": {"duration": "90 phút", "price": "750.000 VND"},
    "Chăm Sóc Da Mặt Cơ Bản": {"duration": "60 phút", "price": "500.000 VND"},
    "Tắm Trắng": {"duration": "120 phút", "price": "1.500.000 VND"},
}

@tool
def list_available_services(query: str = "") -> str:
    """Liệt kê các dịch vụ spa hiện có, thời gian và giá."""
    service_list = "\n".join([
        f"- {name} ({data['duration']}, {data['price']})" 
        for name, data in AVAILABLE_SERVICES.items()
    ])
    return f"Các dịch vụ hiện có tại Spa:\n{service_list}"

class BookAppointmentSchema(BaseModel):
    """Định nghĩa input cần thiết để đặt lịch spa."""
    customer_name: str = Field(description="Tên đầy đủ của khách hàng.")
    service_name: str = Field(description="Tên dịch vụ mà khách hàng muốn đặt (Phải khớp chính xác với tên dịch vụ có sẵn).") 
    date_time: str = Field(description="Ngày và giờ đặt lịch (Ví dụ: '25/12/2025 lúc 14:00').")

@tool(args_schema=BookAppointmentSchema)
def book_spa_appointment(customer_name: str, service_name: str, date_time: str) -> str:
    """
    Đặt lịch cho một dịch vụ spa cụ thể vào ngày giờ đã định. 
    Kiểm tra tính hợp lệ, khả dụng của dịch vụ và lưu vào Database.
    """
    db = SessionLocal()
    try:
        # --- 1. KIỂM TRA VÀ CHUẨN HÓA DỊCH VỤ (FIX TÊN) ---
        normalized_service_name_input = service_name.strip().lower()
        found_key = None
        for key in AVAILABLE_SERVICES.keys():
            if key.strip().lower() == normalized_service_name_input:
                found_key = key
                break
                
        if not found_key:
            return f"Lỗi: Dịch vụ '{service_name}' không hợp lệ. Vui lòng chọn một dịch vụ từ danh sách hiện có."
        
        # Cập nhật service_name thành tên CHUẨN trong dữ liệu gốc
        service_name = found_key
        details = AVAILABLE_SERVICES[service_name]
        
        # --- 2. KIỂM TRA TRÙNG LỊCH (Trong DB) ---
        existing_appt = db.query(Appointment).filter(Appointment.date_time == date_time).first()
        if existing_appt:
            return f"Lỗi: Lịch hẹn vào {date_time} đã có khách ({existing_appt.customer_name}). Vui lòng chọn thời gian khác."
            
        # --- 3. TIẾN HÀNH ĐẶT LỊCH (Lưu vào DB) ---
        new_appointment = Appointment(
            customer_name=customer_name,
            service_name=service_name,
            date_time=date_time,
            price=details['price'],
            duration=details['duration']
        )
        
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        
        # --- 4. CẬP NHẬT st.session_state và PHẢN HỒI ---
        # Cập nhật lại session_state sau khi lưu DB để hiển thị trên sidebar
        st.session_state.SCHEDULED_APPOINTMENTS = get_appointments_from_db()
        
        # Phản hồi xác nhận
        return (
            f"XÁC NHẬN ĐẶT LỊCH THÀNH CÔNG (Đã lưu vào Database):\n"
            f"Khách hàng: {customer_name}\n"
            f"Dịch vụ: {service_name}\n"
            f"Thời gian: {date_time}\n"
            f"Chi tiết: {details['duration']}, {details['price']}\n"
            f"Spa rất hân hạnh được phục vụ quý khách!"
        )
    finally:
        db.close()

@tool
def check_all_appointments(query: str = "") -> str:
    """Kiểm tra và liệt kê tất cả các lịch hẹn đã được đặt (Đọc từ Database)."""
    appointments = get_appointments_from_db()
    
    if not appointments:
        return "Hiện tại chưa có lịch hẹn nào được đặt."
    
    return "Danh sách lịch hẹn đã đặt:\n" + "\n".join([
        f"Khách: {appt['customer_name']} | Dịch vụ: {appt['service_name']} | Lúc: {appt['date_time']}"
        for appt in appointments
    ])

# --- 2. KHỞI TẠO AGENT (PHẦN FIX API KEY VẪN GIỮ NGUYÊN) ---
@st.cache_resource
def initialize_spa_agent():
    """Khởi tạo mô hình ngôn ngữ và Agent. Dùng cache để chỉ khởi tạo 1 lần."""
    
    # Lấy khóa API trực tiếp từ biến môi trường
    GEMINI_KEY = os.getenv("GEMINI_API_KEY")

    # 1. Khởi tạo LLM (Buộc truyền key)
    if GEMINI_KEY:
        # Sửa đổi: Truyền trực tiếp key vào google_api_key argument
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            temperature=0,
            google_api_key=GEMINI_KEY # Đây là phần fix quan trọng nhất
        )
    # elif os.getenv("OPENAI_API_KEY"):
    #     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    else:
        # Nếu không tìm thấy khóa, hiển thị lỗi trên web
        st.error(
            "⚠️ LỖI CẤU HÌNH: Vui lòng thiết lập biến môi trường GEMINI_API_KEY "
            "trong Terminal trước khi chạy ứng dụng. Ví dụ: $env:GEMINI_API_KEY=\"<KHÓA_CỦA_BẠN>\""
        )
        return None

    # 2. Định nghĩa các công cụ (Tools)
    tools = [list_available_services, book_spa_appointment, check_all_appointments]
    
    # 3. Định nghĩa vai trò (System Prompt)
    system_prompt = (
        "Bạn là 'Spa Booking Agent', một trợ lý AI thân thiện và chuyên nghiệp. "
        "Nhiệm vụ của bạn là hỗ trợ khách hàng: "
        "1. Liệt kê các dịch vụ có sẵn. "
        "2. Đặt lịch hẹn bằng tool `book_spa_appointment`. "
        "3. **QUAN TRỌNG:** Để đặt lịch, bạn PHẢI có đủ 3 thông tin: Tên khách, Dịch vụ, Ngày/Giờ. "
        "Nếu thiếu bất kỳ thông tin nào, hãy hỏi khách hàng một cách lịch sự để thu thập đủ. "
        "4. Giao tiếp bằng tiếng Việt chuẩn."
    )
    
    # 4. Khởi tạo Agent
    agent_executor = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS, 
        verbose=False,
        agent_kwargs={"system_message": system_prompt},
        handle_parsing_errors=True
    )
    
    return agent_executor

# --- 3. GIAO DIỆN STREAMLIT (WEB) ---

st.set_page_config(page_title="Spa AI Booking Agent", layout="wide")
st.title("🧖‍♀️ Spa AI Booking Agent")

# Khởi tạo Agent và kiểm tra lỗi cấu hình
spa_agent = initialize_spa_agent()

if spa_agent:
    
    # Khởi tạo lịch sử chat
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Xin chào! Tôi là Spa Booking Agent. Tôi có thể giúp bạn đặt lịch spa hôm nay."}
        ]

    # Hiển thị lịch sử chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Xử lý input của người dùng
    if prompt := st.chat_input("Hỏi tôi về dịch vụ hoặc đặt lịch..."):
        
        # Thêm tin nhắn người dùng vào lịch sử
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Chạy Agent và nhận phản hồi
        with st.chat_message("assistant"):
            with st.spinner("Agent đang xử lý..."):
                try:
                    # Gọi Agent với input của người dùng
                    result = spa_agent.invoke({"input": prompt})
                    response = result['output']
                except Exception as e:
                    # Lỗi này có thể là do API Key sai/hết hạn hoặc kết nối
                    response = f"Lỗi hệ thống khi gọi AI: Vui lòng kiểm tra lại GEMINI_API_KEY, trạng thái của khóa, hoặc kết nối mạng. Chi tiết: {e}"

            # Hiển thị phản hồi
            st.markdown(response)
        
        # Thêm phản hồi của Agent vào lịch sử
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Sidebar để hiển thị các lịch hẹn đã đặt
    with st.sidebar:
        st.header("Lịch Hẹn Đã Đặt")
        # Sidebar luôn đọc từ st.session_state, đã được cập nhật từ DB
        if st.session_state.SCHEDULED_APPOINTMENTS:
            for i, appt in enumerate(st.session_state.SCHEDULED_APPOINTMENTS):
                st.markdown(f"**Lịch #{i+1}**")
                # Hiển thị chi tiết dưới dạng Markdown
                st.markdown(f"Khách: **{appt['customer_name']}**")
                st.markdown(f"Dịch vụ: **{appt['service_name']}**")
                st.markdown(f"Thời gian: **{appt['date_time']}**")
                st.markdown("---")
        else:
            st.info("Chưa có lịch hẹn nào được đặt.")