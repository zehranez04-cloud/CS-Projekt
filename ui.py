#gemeinsame Farben für die ganze App
FARBEN = {"primary": "#1f77b4","secondary": "#ff7f0e","success": "#2ca02c","danger": "#d62728","warning": "#ffbb78","info": "#17becf", "light": "#f7f7f7", "dark": "#343a40"}
import streamlit as st



# Ebene 3: einheitlicher Stil für alle Plotly-Diagramme
def diagramm_stil(fig):
    fig.update_layout(template="simple_white", margin=dict(t=30, b=10),
                      colorway=[FARBEN["primaer"], FARBEN["grau"]])
    return fig


# Ebene 4: eigenes CSS
def css_laden():
    st.html("""
    <style>
    .badge {padding: 4px 12px; border-radius: 12px; color: white; font-weight: 600;}
    .rot {background: #C62828;} .gelb {background: #F9A825;} .gruen {background: #2E7D32;}
    </style>
    """)


def badge(text, farbe):
    """Zeigt ein farbiges Etikett an, z.B. badge("Erhebliche Zweifel", "rot")."""
    st.html(f'<span class="badge {farbe}">{text}</span>')