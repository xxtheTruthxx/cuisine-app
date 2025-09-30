import streamlit as st
import json

def load_data(filename: str) -> dict:
  with open(filename, "r") as f:
    data = json.load(f)
  return data

def app():
    st.set_page_config(
        page_title="")
    st.header(body="Flavors of the Globe", help="Discover the tastes of the world in one place!", divider="gray")
    st.markdown("""
        <style>
            button p{
                font-weight: 700 !important;
            }
        </style>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        st.caption("""
                <p style='font-weight: 600'>
                  Flavors of the Globe are like magical gateways that take us on a journey through cultures and traditions.
                  Discover with us the richness of culinary experiences hidden in every bite!
                </p>
            """, unsafe_allow_html=True)

    with st.container(border=True):
        for c, j in enumerate(load_data("data.json").values(), 0):
            with st.container(border=True):
                st.title(j.get("title"))
                tab1, tab2 = st.tabs(["Introduction", "Read More"])
                with tab1:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"<p style='font-weight: 600'>{j.get('description')}</p>", unsafe_allow_html=True)
                    with col2:
                        img = j.get("img")
                        st.image(image=img["path"], caption=img["caption"].upper())
                with tab2:
                    st.write(j.get("info"))
                            
if __name__ == "__main__":
    app()
