import streamlit as st

# 1. App-Konfiguration für das Smartphone
st.set_page_config(
    page_title="ESUP - Premium Health",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Das kontraststarke, klinische Medizin-Design
st.markdown("""
    <style>
    /* Hintergrund & Haupttext: Höchster Kontrast */
    .stApp {
        background-color: #0F172A; /* Tiefes, seriöses Dunkelblau-Grau */
        color: #F8FAFC; /* Klares Haupt-Weiß */
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    
    .block-container {
        padding: 2rem 1.2rem !important;
        max-width: 440px !important;
        margin: 0 auto;
    }
    
    h1 {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
        color: #F8FAFC !important;
        margin-bottom: 0px !important;
    }
    
    h3 {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #F1F5F9 !important; /* Deutlich aufgehellte Sektions-Titel */
        margin-top: 30px !important;
        margin-bottom: 15px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* RADIKALER FIX: Macht alle Beschriftungen von Eingabefeldern (Gewicht, Regler etc.) schneeweiß */
    .stNumberInput label, .stSlider label, .stSelectbox label, .stCheckbox p {
        color: #FFFFFF !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
    }
    
    /* Schlichtes Verzeichnis-Box-Design */
    .supp-box {
        background: #1E293B;
        border: 1px solid #334155;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-size: 0.9rem;
        color: #F1F5F9;
    }
    
    /* Klinischer Befund-Bericht (Keine Werbung) */
    .clinical-report {
        background: #1E293B;
        border-left: 3px solid #38BDF8; /* Seriöses Medizin-Blau */
        padding: 14px;
        border-radius: 8px;
        margin-top: 12px;
    }
    
    .clinical-report h4 {
        margin: 0 0 5px 0 !important;
        font-size: 1rem;
        color: #F8FAFC !important;
    }
    
    .clinical-report p {
        font-size: 0.88rem;
        color: #E2E8F0; /* Helles Off-White für perfekte Lesbarkeit */
        margin: 4px 0 !important;
        line-height: 1.4;
    }
    
    /* Professioneller Auswertungs-Button */
    .stButton>button {
        background-color: #38BDF8 !important; 
        color: #0F172A !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        width: 100% !important;
        padding: 0.6rem !important;
    }
    
    /* Dezenter, lesbarer Disclaimer */
    .custom-disclaimer {
        font-size: 0.8rem;
        color: #94A3B8; /* Klares Silbergrau statt unleserlichem Schiefergrau */
        line-height: 1.4;
        margin-top: 35px;
        border-top: 1px solid #334155;
        padding-top: 15px;
    }
    
    [data-testid="collapsedControl"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SCIENTIFIC DATABASE
# ==========================================
SUPP_DB = {
    "Kreatin Monohydrat": {
        "wirkung": "Unterstützt die Resynthese von ATP bei kurzen, intensiven Muskelbelastungen.",
        "koerper": "Erhöht den zellulären Phosphokreatinspeicher und begünstigt die Flüssigkeitseinlagerung im Muskelgewebe."
    },
    "Omega-3 Fettsäuren": {
        "wirkung": "Liefert die essenziellen Fettsäuren EPA und DHA.",
        "koerper": "Trägt zur Regulierung von Entzündungsprozessen und zur Aufrechterhaltung der normalen Herzfunktion bei."
    },
    "Vitamin D3 + K2": {
        "wirkung": "Unterstützt den Calciumstoffwechsel und die Funktion des Immunsystems.",
        "koerper": "Fördert die Calciumaufnahme im Darm. Vitamin K2 unterstützt die Einlagerung in das Knochengerüst."
    },
    "Kollagen-Hydrolysat": {
        "wirkung": "Liefert Aminosäuren für das körpereigene Bindegewebe.",
        "koerper": "Wird im Extrazellulärraum für die Struktur von Haut, Sehnen und Knorpelgewebe verwendet."
    },
    "Molkenprotein (Whey)": {
        "wirkung": "Proteinquelle mit hoher biologischer Wertigkeit zur Unterstützung der Proteinsynthese.",
        "koerper": "Wird schnell in Aminosäuren zerlegt und steht der Muskulatur zeitnah zur Regeneration zur Verfügung."
    },
    "Magnesium (Bisglycinat)": {
        "wirkung": "Trägt zur normalen Muskelfunktion und Verringerung von Ermüdung bei.",
        "koerper": "Reguliert als Co-Faktor in über 300 Enzymsystemen die neuronale Erregungsleitung."
    },
    "Zink (Picolinat)": {
        "wirkung": "Essentielles Spurenelement für den Makronährstoff-Stoffwechsel.",
        "koerper": "Unterstützt die zelluläre Eiweißsynthese und die normale Funktion des Immunsystems."
    }
}

# --- APP BRANDING ---
st.markdown('<h1>🧬 ESUP</h1>', unsafe_allow_html=True)
st.markdown('<p translate="no" style="font-size: 0.9rem; color: #38BDF8; font-weight: 600; margin-top: -5px; margin-bottom: 20px;">Easy Supplements</p>', unsafe_allow_html=True)
st.write("Wissenschaftliche Orientierungshilfe zur Strukturierung der sportlichen Nahrungsergänzung.")

# ==========================================
# NEUE REIHENFOLGE - BEREICH 1: DIE AUSWERTUNG (Sofortiger Nutzen!)
# ==========================================
st.subheader("Analyse & Parameter")

gewicht = st.number_input("Körpergewicht (kg):", min_value=40, max_value=150, value=80, step=1)
sport_tage = st.slider("Trainingsfrequenz (Tage pro Woche):", 0, 7, 3)

st.markdown("<p style='font-size:0.9rem; font-weight:600; color:#F1F5F9; margin-bottom:5px; margin-top:15px;'>Ernährungsspezifische Faktoren:</p>", unsafe_allow_html=True)
kein_fisch = st.checkbox("Verzicht auf Fischkonsum / Fischallergie")
wenig_sonne = st.checkbox("Geringe Sonnenexposition (< 15 Min. täglich)")

st.markdown(" ")
arzt_check = st.checkbox("Ich bestätige, dass diese Berechnung eine unverbindliche Orientierung darstellt.")

if st.button("Unverbindliche Auswertung generieren"):
    if not arzt_check:
        st.error("⚠️ Bitte bestätige zuerst die Kenntnisnahme des Hinweises.")
    else:
        st.success("Auswertung erfolgreich generiert.")
        st.markdown("### 📋 Ermittelte Richtwerte")
        
        # 1. Kreatin
        if sport_tage >= 3:
            kr_menge = round(gewicht * 0.05, 1)
            st.markdown(f"""<div class="clinical-report"><h4>Kreatin Monohydrat</h4><p><b>Richtwert:</b> ca. {kr_menge}g täglich.</p><p>Einnahme vorzugsweise zeitnah nach einer Trainingseinheit.</p></div>""", unsafe_allow_html=True)

        # 2. Kollagen
        kol_kapseln = 3 if sport_tage >= 4 else 2
        st.markdown(f"""<div class="clinical-report"><h4>Kollagen-Hydrolysat</h4><p><b>Richtwert:</b> ca. {kol_kapseln} Kapseln täglich.</p><p>Zur Unterstützung der Aminosäurenzufuhr für das Bindegewebe.</p></div>""", unsafe_allow_html=True)

        # 3. Whey Protein
        if sport_tage >= 1:
            st.markdown("""<div class="clinical-report"><h4>Molkenprotein (Whey)</h4><p><b>Richtwert:</b> 1 Shake (30g) an Trainingstagen.</p><p>Dient der Deckung des sportbedingt erhöhten Proteinbedarfs.</p></div>""", unsafe_allow_html=True)

        # 4. Omega-3
        if kein_fisch:
            st.markdown("""<div class="clinical-report"><h4>Veganes Algenöl (Omega-3)</h4><p><b>Richtwert:</b> 2 Kapseln täglich.</p><p>Zufuhr von EPA/DHA bei Verzicht auf maritime Lebensmittel.</p></div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="clinical-report"><h4>Omega-3 Fettsäuren (Fischöl)</h4><p><b>Richtwert:</b> 1 Kapsel täglich.</p><p>Zur Absicherung der Versorgung mit essenziellen Fettsäuren.</p></div>""", unsafe_allow_html=True)

        # 5. Vitamin D3
        if wenig_sonne:
            st.markdown("""<div class="clinical-report"><h4>Vitamin D3 + K2</h4><p><b>Richtwert:</b> 1 Kapsel jeden zweiten Tag.</p><p>Ausgleich bei geringer körpereigener Synthese durch Sonnenlicht.</p></div>""", unsafe_allow_html=True)

# ==========================================
# NEUE REIHENFOLGE - BEREICH 2: DAS LEXIKON (Jetzt unten zum Nachschlagen!)
# ==========================================
st.subheader("Substanz-Nachschlagewerk")

with st.expander("📖 Übersicht der analysierten Substanzen öffnen"):
    for name in sorted(list(SUPP_DB.keys())):
        st.markdown(f'<div class="supp-box"><b>{name}</b></div>', unsafe_allow_html=True)

auswahl = st.selectbox(
    "Substanz auswählen für Detail-Analyse:", 
    ["Bitte wählen..."] + sorted(list(SUPP_DB.keys()))
)

if auswahl != "Bitte wählen...":
    details = SUPP_DB[auswahl]
    st.markdown(f"""
    <div class="clinical-report">
        <h4>{auswahl}</h4>
        <p><b>Physiologischer Zweck:</b> {details['wirkung']}</p>
        <p><b>Biochemischer Prozess:</b> {details['koerper']}</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER & CREDITS
# ==========================================
st.markdown(f"""
<div class="custom-disclaimer">
    <b>Medizinischer Hinweis:</b> Alle hier ausgegebenen Werte, Richtwerte und Texte dienen ausschließlich der allgemeinen Information und wissenschaftlichen Orientierung. Sie stellen keine medizinische Beratung, Diagnose oder verbindliche Dosierungsempfehlung dar. Jede Anpassung der Ernährung oder Einnahme von Nahrungsergänzungsmitteln sollte bei Unsicherheiten oder Vorerkrankungen individuell mit einem Arzt oder qualifizierten Mediziner abgeklärt werden. Alle Inhalte dieser App (ESUP) sind unverbindlich.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col2:
    st.caption("***Built by K.K.***")
