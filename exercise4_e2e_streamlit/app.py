# import streamlit as st

# st.set_page_config(page_title="Tiny Calc", page_icon="🧮")
# st.title("Tiny Calculator")

# op = st.selectbox("Operation", ["add", "div", "clamp"], key="operation")
# a  = st.number_input("A", value=0.0, key="a")
# b  = st.number_input("B", value=0.0, key="b")
# c = None
# if op == "clamp":
#     c = st.number_input("HIGH (only for clamp; LOW is B)", value=10.0, key="high")

# if st.button("Compute", key="compute"):
#     def compute(op, a, b, c=None):
#         if op == "add":
#             return a + b
#         if op == "div":
#             return "ERROR" if b == 0 else a / b
#         if op == "clamp":
#             return "ERROR" if b > c else max(b, min(a, c))
#         return "ERROR"
#     res = compute(op, a, b, c)
#     st.text(f"Result: {res}")

import streamlit as st

st.set_page_config(page_title="Tiny Calc", page_icon="🧮")
st.title("Tiny Calculator")

# Stable anchors for Cypress (safe with older Streamlit)
st.markdown('<div data-cy="op"></div>', unsafe_allow_html=True)
op = st.selectbox("Operation", ["add", "div", "clamp"], key="operation")

st.markdown('<div data-cy="a"></div>', unsafe_allow_html=True)
a = st.number_input("A", value=0.0, key="a")

st.markdown('<div data-cy="b"></div>', unsafe_allow_html=True)
b = st.number_input("B", value=0.0, key="b")

c = None
if op == "clamp":
    st.markdown('<div data-cy="high"></div>', unsafe_allow_html=True)
    c = st.number_input("HIGH (only for clamp; LOW is B)", value=10.0, key="high")

def compute(op, a, b, c=None):
    if op == "add":
        return a + b
    if op == "div":
        return "ERROR" if b == 0 else a / b
    if op == "clamp":
        return "ERROR" if b > c else max(b, min(a, c))
    return "ERROR"

if st.button("Compute", key="compute"):
    res = compute(op, a, b, c)
    # Use simple text (compatible with older Streamlit)
    st.text(f"Result: {res}")
