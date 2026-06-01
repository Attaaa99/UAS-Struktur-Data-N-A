import streamlit as st
import pandas as pd
import math

# =====================
# KONFIGURASI HALAMAN
# =====================
st.set_page_config(
    page_title="RPN Calculator",
    page_icon="🧮",
    layout="wide"
)

# =====================
# CSS
# =====================
st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
}

h1,h2,h3{
    color:white;
}

[data-testid="stSidebar"]{
    background-color:#111827;
}

.stButton button{
    width:100%;
    border-radius:10px;
    background:#2563eb;
    color:white;
    font-weight:bold;
}

.result-box{
    background:#1e293b;
    color:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =====================
# SESSION STATE
# =====================
if "history" not in st.session_state:
    st.session_state.history = []

# =====================
# FUNGSI RPN
# =====================
def evaluate_rpn(expression):

    stack = []

    tokens = expression.split()

    for token in tokens:

        if token.replace(".", "", 1).isdigit():
            stack.append(float(token))

        elif token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)

        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)

        elif token == "^":
            b = stack.pop()
            a = stack.pop()
            stack.append(a ** b)

        elif token == "sqrt":
            a = stack.pop()
            stack.append(math.sqrt(a))

        elif token == "sin":
            a = stack.pop()
            stack.append(math.sin(math.radians(a)))

        elif token == "cos":
            a = stack.pop()
            stack.append(math.cos(math.radians(a)))

        elif token == "tan":
            a = stack.pop()
            stack.append(math.tan(math.radians(a)))

        elif token == "log":
            a = stack.pop()
            stack.append(math.log10(a))

        else:
            raise ValueError(f"Operator {token} tidak dikenal")

    return stack[0]

# =====================
# SIDEBAR
# =====================
menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Kalkulator",
        "Riwayat",
        "Tentang"
    ]
)

# =====================
# MENU KALKULATOR
# =====================
if menu == "Kalkulator":

    st.title("🧮 RPN Calculator")

    st.write("""
Contoh Input:

3 4 +

10 2 /

5 5 *

9 sqrt

30 sin

2 3 ^
""")

    expression = st.text_input(
        "Masukkan Ekspresi RPN"
    )

    if st.button("Hitung"):

        try:

            hasil = evaluate_rpn(expression)

            st.markdown(
                f"""
                <div class="result-box">
                Hasil = {hasil}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.session_state.history.append(
                {
                    "Ekspresi": expression,
                    "Hasil": hasil
                }
            )

        except Exception as e:
            st.error(e)

# =====================
# RIWAYAT
# =====================
elif menu == "Riwayat":

    st.title("📜 Riwayat Perhitungan")

    if len(st.session_state.history) > 0:

        df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("Belum ada data.")

# =====================
# TENTANG
# =====================
elif menu == "Tentang":

    st.title("ℹ️ Tentang Program")

    st.write("""
Aplikasi Reverse Polish Notation Calculator.

Fitur:
- Penjumlahan
- Pengurangan
- Perkalian
- Pembagian
- Pangkat
- Akar
- Sin
- Cos
- Tan
- Logaritma

Dibuat menggunakan:
- Python
- Streamlit
- Stack Data Structure

Dibuat oleh:
    Naufal Atha
""")

