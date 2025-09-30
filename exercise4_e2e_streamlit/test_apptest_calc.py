from streamlit.testing.v1 import AppTest

def run_app():
    # Load and render the app once
    return AppTest.from_file("exercise4_e2e_streamlit/app.py").run()

def test_add():
    at = run_app()
    # Select operation
    at.selectbox("operation").select("add").run()
    # Fill inputs
    at.number_input("a").set_value(5).run()
    at.number_input("b").set_value(10).run()
    # Click compute
    at.button("compute").click().run()
    # Assert result is rendered
    assert any("Result: 15" in e.value for e in at.text)

def test_div():
    at = run_app()
    at.selectbox("operation").select("div").run()
    at.number_input("a").set_value(9).run()
    at.number_input("b").set_value(3).run()
    at.button("compute").click().run()
    assert any("Result: 3" in m.value for m in at.text)

def test_div_by_zero():
    at = run_app()
    at.selectbox("operation").select("div").run()
    at.number_input("a").set_value(1).run()
    at.number_input("b").set_value(0).run()
    at.button("compute").click().run()
    assert any("Result: ERROR" in m.value for m in at.text)

def test_clamp():
    at = run_app()
    at.selectbox("operation").select("clamp").run()
    at.number_input("a").set_value(11).run()
    at.number_input("b").set_value(0).run()
    at.number_input("high").set_value(10).run()
    at.button("compute").click().run()
    assert any("Result: 10" in m.value for m in at.text)
