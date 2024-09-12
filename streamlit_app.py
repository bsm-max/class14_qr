import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# QR 코드 생성 함수
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Streamlit 앱 레이아웃
def main():
    st.title("QR 코드 생성기")
    st.write("텍스트나 URL을 입력하면 QR 코드를 생성할 수 있습니다.")
    
    # 사용자 입력
    data = st.text_input("QR 코드에 넣을 텍스트 또는 URL을 입력하세요")
    
    if st.button("QR 코드 생성"):
        if data:
            # QR 코드 생성
            img = generate_qr_code(data)
            
            # 이미지를 스트림으로 변환하여 표시
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            st.image(buffer.getvalue(), caption="생성된 QR 코드", use_column_width=True)
            
            # QR 코드 다운로드 버튼 추가
            btn = st.download_button(
                label="QR 코드 다운로드",
                data=buffer.getvalue(),
                file_name="qr_code.png",
                mime="image/png"
            )
        else:
            st.warning("텍스트 또는 URL을 입력하세요.")
    
if __name__ == "__main__":
    main()  # 이 부분이 들여쓰기로 문제를 해결합니다.
