import streamlit as st
#from rag_no_chain import get_rag_answer
from rag_llm_recent import get_rag_answer
import random
from collections import deque
from law_rag import generate_answer_with_retrieved_docs
from PIL import Image

def run_driver_assistant_app():
    st.set_page_config(page_title="운전자 도우미 챗봇", page_icon="🚗", layout="wide")

    # --- CSS 스타일 ---
    st.markdown("""
    <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }
        .stButton>button {
            border: none;
            border-radius: 10px;
            padding: 20px;
            background-color: #EAF2F8;
            transition: all 0.3s;
            height: 100%;
            width: 100%;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
            background-color: #D4E6F1;
        }
        .stButton p {
            font-size: 1.1rem;
            font-weight: bold;
            color: #495057;
        }
        .card-description {
            font-size: 0.9rem;
            color: #6c757d;
            margin-top: 10px;
        }
        [data-testid="stAlert"] {
            background-color: #F0F8FF;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- 세션 상태 초기화 ---
    if "page" not in st.session_state:
        st.session_state.page = "home"  # home, driving, legal
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "recent_questions" not in st.session_state:
        st.session_state.recent_questions = deque(maxlen=10)
    if "question_count" not in st.session_state:
        st.session_state.question_count = 0
    if "prefilled_question" not in st.session_state:
        st.session_state.prefilled_question = None

    # --- 페이지 전환 및 헬퍼 함수 ---
    def go_to(page):
        st.session_state.page = page
        st.rerun()

    def ask_recent_question(question):
        st.session_state.prefilled_question = question
        st.session_state.page = "driving"
        st.rerun()

    # --- 사이드바: 운전자 프로필 ---
    with st.sidebar:
        st.header("👤 운전자 프로필")
        st.image("https://placehold.co/100x100/28B463/FFFFFF?text=Lv.1", caption="초보 운전자")
        st.metric(label="총 질문 횟수", value=f"{st.session_state.question_count} 회")
        st.markdown("---")
        st.info("질문을 많이 할수록 레벨이 올라가요!")

    # --- 홈 화면 ---
    if st.session_state.page == "home":
        #st.image(Image.open("C:\\SK_17\\LMM\\3rd_proj\\배너2.png"), use_container_width=True)
        st.image(Image.open("/root/project3/image/banner.png"), use_container_width=True)
        #st.markdown("<h1 style='text-align:center; color:#2E86C1;'>🚘 초보 운전자 도우미</h1>", unsafe_allow_html=True)
        #st.markdown("<p style='text-align:center; color:#566573;'>무엇이든 물어보세요! AI가 운전 중 궁금증을 해결해 드립니다.</p>", unsafe_allow_html=True)
        st.write("---")

        # 기능 선택 카드
        col1, col2 = st.columns(2)
        with col1:
            btn_col1, btn_col2, btn_col3 = st.columns([1, 1.5, 1])
            with btn_col2:
                if st.button("주행 중 켜놓기", use_container_width=True):
                    go_to("driving")
            st.markdown("""
                <div class='card-description' style='text-align:center;'>
                    <p>🛣️ <b>주행 중 켜놓기</b></p>
                    <p>실시간으로 궁금한 점을 질문하고 즉시 답변을 받으세요.</p>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            btn_col1, btn_col2, btn_col3 = st.columns([1, 1.5, 1])
            with btn_col2:
                if st.button("질문에 대한 법적 근거", use_container_width=True):
                    go_to("legal")
            st.markdown("""
                <div class='card-description' style='text-align:center;'>
                    <p>⚖️ <b>법적 근거</b></p>
                    <p>사고 발생 시 대처법과 그와 관련된 법적 근거를 안내합니다.</p>
                </div>
            """, unsafe_allow_html=True)
        st.write("---")

        # 오늘의 운전 팁
        tips = [
            "비 오는 날에는 평소보다 20% 이상 감속 운행하세요.",
            "터널에 진입하기 전에는 선글라스를 벗고 전조등을 켜세요.",
            "주차 시에는 사이드미러를 접어 다른 차의 통행을 배려해주세요.",
            "고속도로에서 졸음이 올 땐, 가까운 졸음쉼터나 휴게소를 이용하세요.",
            "'어린이 보호구역'에서는 시속 30km 이하로 서행해야 합니다."
        ]
        st.info(f"💡 **오늘의 운전 팁:** {random.choice(tips)}")
        st.write("---")

        # 최근 질문 목록
        st.subheader("최근 질문 목록")
        if st.session_state.recent_questions:
            for q in list(st.session_state.recent_questions):
                if st.button(q, use_container_width=True, key=f"recent_{q}"):
                    ask_recent_question(q)
        else:
            st.markdown("아직 질문 기록이 없습니다.")

    # --- 주행 중 모드 ---
    elif st.session_state.page == "driving":
        st.markdown("<h1 style='text-align:center; color:#28B463;'>🚦 주행 보조 챗봇</h1>", unsafe_allow_html=True)

        if st.button("⬅️ 홈으로 돌아가기"):
            st.session_state.chat_history = []
            go_to("home")

        chat_col, side_col = st.columns([2, 1])

        with side_col:
            st.subheader("💡 추천 질문")
            if st.button("내리막길 기어", use_container_width=True):
                ask_recent_question("내리막길 기어")
            if st.button("앞 차가 갑자기 브레이크를 밟았어", use_container_width=True):
                ask_recent_question("앞 차가 갑자기 브레이크를 밟았어")
            if st.button("졸음 운전 방지 팁", use_container_width=True):
                ask_recent_question("졸음 운전 방지 팁")

        with chat_col:
            chat_container = st.container(height=500)
            with chat_container:
                for role, msg in st.session_state.chat_history:
                    st.chat_message(role).write(msg)

            # 사용자 입력 처리
            if st.session_state.prefilled_question:
                user_input = st.session_state.prefilled_question
                st.session_state.prefilled_question = None
            else:
                user_input = st.chat_input("무엇이 궁금한가요?")

            if user_input:
                st.session_state.chat_history.append(("user", user_input))
                if user_input not in st.session_state.recent_questions:
                    st.session_state.recent_questions.appendleft(user_input)
                st.session_state.question_count += 1
                st.rerun()

            # AI 응답
            if st.session_state.chat_history and st.session_state.chat_history[-1][0] == "user":
                last_user_input = st.session_state.chat_history[-1][1]
                with st.spinner("답변을 찾고 있어요..."):
                    answer = get_rag_answer(last_user_input, search_mode="similarity")
                    st.session_state.chat_history.append(("assistant", answer))
                    st.rerun()

    # --- 사고 후 법률 조언 모드 ---
    elif st.session_state.page == "legal":
        st.markdown("<h1 style='text-align:center; color:#C0392B;'>⚖️ 사고 후 법률 조언</h1>", unsafe_allow_html=True)
        
        if st.button("⬅️ 홈으로 돌아가기"):
            go_to("home")
        
        chat_col, side_col = st.columns([2, 1])
        
        with chat_col:
            # 채팅 기록을 담을 컨테이너 (스크롤 가능)
            chat_container = st.container(height=500)
            with chat_container:
                for role, msg in st.session_state.chat_history:
                    st.chat_message(role).write(msg)

            user_input = st.chat_input("법적 근거로 궁금한 점을 질문하세요.")

            if st.session_state.prefilled_question:
                user_input = st.session_state.prefilled_question
                st.session_state.prefilled_question = None

            if user_input:
                st.session_state.chat_history.append(("user", user_input))
                if user_input not in st.session_state.recent_questions:
                    st.session_state.recent_questions.appendleft(user_input)
                st.session_state.question_count += 1
                st.rerun()
            # AI 응답
            if st.session_state.chat_history and st.session_state.chat_history[-1][0] == "user":
                last_user_input = st.session_state.chat_history[-1][1]
                with st.spinner("답변을 찾고 있어요..."):
                    answer = generate_answer_with_retrieved_docs(last_user_input)
                    st.session_state.chat_history.append(("assistant", answer))
                    st.rerun()
                    
    # 🚀 최근 질문 목록 표시
        with side_col:
            st.subheader("최근 질문 목록")
            if st.session_state.recent_questions:
                for q in list(st.session_state.recent_questions):
                    if st.button(q, use_container_width=True, key=f"legal_recent_{q}"):
                        # 이 질문의 법적 근거를 검색하도록 기능 연결
                        answer = get_rag_answer(q, search_mode="legal")  # 예: search_mode를 legal로 바꿔서 법률 문서만 검색
                        st.write(f"📜 **{q}** 관련 법적 근거:\n\n{answer}")
            else:
                st.markdown("아직 질문 기록이 없습니다.")

    

# 실행
if __name__ == "__main__":
    run_driver_assistant_app()


