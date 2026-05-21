import streamlit as st

# 1. App-Konfiguration für das Smartphone
st.set_page_config(
    page_title="ESUP - Premium Health Advisor",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Das neue, dynamische Dashboard-Design (Apple Health / Premium-Sport-Stil)
st.markdown("""
    <style>
    /* Basis-Setup: Hochwertig, dunkel und athletisch */
    .stApp {
        background-color: #0B0F19; /* Tiefes Midnight-Black */
        color: #F8FAFC; /* Klares Haupt-Weiß */
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    
    .block-container {
        padding: 2rem 1.2rem !important;
        max-width: 440px !important;
        margin: 0 auto;
    }
    
    h1 {
        font-size: 2rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        color: #FFFFFF !important;
        margin-bottom: 0px !important;
    }
    
    h3 {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: #38BDF8 !important; /* Elektrisierendes Medizin-Blau als Akzent */
        margin-top: 30px !important;
        margin-bottom: 15px !important;
        letter-spacing: 0.3px;
    }
    
    /* Schneeweiße, perfekt lesbare Beschriftungen für alle Felder */
    .stNumberInput label, .stSlider label, .stSelectbox label, .stCheckbox p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    /* Edle Dashboard-Ergebnis-Karten (Wirkt wie eine High-Tech App) */
    .dashboard-card {
        background: linear-gradient(135deg, #1E293B 0%, #111827 100%);
        border: 1px solid #334155;
        padding: 16px;
        border-radius: 14px;
        margin-top: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    
    .dashboard-card h4 {
        margin: 0 0 6px 0 !important;
        font-size: 1.1rem;
        color: #FFFFFF !important;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .dashboard-card p {
        font-size: 0.9rem;
        color: #E2E8F0; /* Helles, klares Weiß-Grau für beste Lesbarkeit */
        margin: 4px 0 !important;
        line-height: 1.4;
    }
    
    .target-value {
        background-color: rgba(56, 189, 248, 0.15);
        color: #38BDF8;
        padding: 2px 8px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.85rem;
    }
    
    /* Schlichte, dunkle Boxen fürs Lexikon */
    .lexicon-box {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-size: 0.9rem;
        color: #E2E8F0;
    }
    
    /* Der athletische Aktivierungs-Button */
    .stButton>button {
        background: linear-gradient(90deg, #38BDF8 0%, #3b82f6 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        width: 100% !important;
        padding: 0.7rem !important;
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.2);
        transition: 0.2s all;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(56, 189, 248, 0.3);
    }
    
    /* Dezenter, lesbarer Disclaimer */
    .custom-disclaimer {
        font-size: 0.8rem;
        color: #94A3B8;
        line-height: 1.4;
        margin-top: 40px;
        border-top: 1px solid #1E293B;
        padding-top: 15px;
    }
    
    [data-testid="collapsedControl"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# WISSENSCHAFTLICHE DATENBANK
# ==========================================
SUPP_DB = {
    "Kreatin Monohydrat": {
        "icon": "💪",
        "wirkung": "Unterstützt die Resynthese von ATP bei kurzen, intensiven Muskelbelastungen.",
        "koerper": "Erhöht den zellulären Phosphokreatinspeicher und begünstigt die Flüssigkeitseinlagerung im Muskelgewebe."
    },
    "Omega-3 Fettsäuren": {
        "icon": "🐟",
        "wirkung": "Liefert die essenziellen Fettsäuren EPA und DHA.",
        "koerper": "Trägt zur Regulierung von Entzündungsprozessen und zur Aufrechterhaltung der normalen Herzfunktion bei."
    },
    "Vitamin D3 + K2": {
        "icon": "☀️",
        "wirkung": "Unterstützt den Calciumstoffwechsel und die Funktion des Immunsystems.",
        "koerper": "Fördert die Calciumaufnahme im Darm. Vitamin K2 unterstützt die Einlagerung in das Knochengerüst."
    },
    "Kollagen-Hydrolysat": {
        "icon": "✨",
        "wirkung": "Liefert Aminosäuren für das körpereigene Bindegewebe.",
        "koerper": "Wird im Extrazellulärraum für die Struktur von Haut, Sehnen und Knorpelgewebe verwendet."
    },
    "Molkenprotein (Whey)": {
        "icon": "🥛",
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
st.markdown('<p translate="no" style="font-size: 1rem; color: #38BDF8; font-weight: 700; margin-top: -5px; margin-bottom: 20px;">Easy Supplements</p>', unsafe_allow_html=True)

# ==========================================
# BEREICH 1: DIE DIAGNOSE-KONSOLE
# ==========================================
st.subheader("⚡ DEIN PROFIL-CHECK")

gewicht = st.number_input("Körpergewicht (kg):", min_value=40, max_value=150, value=80, step=1)
sport_tage = st.slider("Trainingsfrequenz (Tage pro Woche):", 0, 7, 3)

st.markdown("<p style='font-size:0.9rem; font-weight:700; color:#FFFFFF; margin-bottom:5px; margin-top:15px;'>Ernährung & Lifestyle:</p>", unsafe_allow_html=True)
kein_fisch = st.checkbox("Verzicht auf Fischkonsum / Fischallergie")
wenig_sonne = st.checkbox("Geringe Sonnenexposition (< 15 Min. täglich)")

st.markdown(" ")
arzt_check = st.checkbox("Ich bestätige, dass diese Berechnung eine unverbindliche Orientierung darstellt.")

if st.button("Unverbindliche Empfehlung berechnen"):
    if not arzt_check:
        st.error("⚠️ Bitte bestätige zuerst die Kenntnisnahme des Hinweises.")
    else:
        st.success("Analyse erfolgreich abgeschlossen.")
        st.markdown("### 📋 DEIN TÄGLICHER ATHLETEN-STACK")
        
        # 1. Kreatin (Dynamischer Badge-Look)
        if sport_tage >= 3:
            kr_menge = round(gewicht * 0.05, 1)
            st.markdown(f"""
            <div class="dashboard-card">
                <h4>💪 Kreatin Monohydrat <span class="target-value">Zielwert: ca. {kr_menge}g</span></h4>
                <p><b>Anwendung:</b> Täglich direkt nach der Belastung einnehmen.</p>
                <p>Unterstützt die ATP-Resynthese bei deiner Frequenz von {sport_tage} Trainingstagen.</p>
            </div>
            """, unsafe_allow_html=True)

        # 2. Kollagen
        kol_kapseln = 3 if sport_tage >= 4 else 2
        st.markdown(f"""
        <div class="dashboard-card">
            <h4>✨ Gelenk-Kollagen <span class="target-value">Zielwert: ca. {kol_kapseln} Kapseln</span></h4>
            <p><b>Anwendung:</b> Morgens unabhängig von den Mahlzeiten einnehmen.</p>
            <p>Sichert die gezielte Aminosäurenversorgung für Sehnen und Knorpelgewebe.</p>
        </div>
        """, unsafe_allow_html=True)

        # 3. Whey Protein
        if sport_tage >= 1:
            st.markdown("""
            <div class="dashboard-card">
                <h4>🥛 Proteinquelle (Whey) <span class="target-value">Zielwert: 1 Shake (30g)</span></h4>
                <p><b>Anwendung:</b> Unmittelbar nach dem Training oder morgens an spielfreien Tagen.</p>
                <p>Unterstützt die Muskelproteinsynthese bei sportlich erhöhtem Bedarf.</p>
            </div>
            """, unsafe_allow_html=True)

        # 4. Omega-3 Logik
        if kein_fisch:
            st.markdown("""
            <div class="dashboard-card">
                <h4>🌱 Veganes Algenöl <span class="target-value">Zielwert: 2 Kapseln</span></h4>
                <p><b>Anwendung:</b> Zu einer fetthaltigen Hauptmahlzeit einnehmen.</p>
                <p>Pflanzliche Absicherung der essenziellen EPA/DHA-Werte bei Fischverzicht.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dashboard-card">
                <h4>🐟 Omega-3 Fischöl <span class="target-value">Zielwert: 1 Kapsel</span></h4>
                <p><b>Anwendung:</b> Zu einer beliebigen Mahlzeit einnehmen.</p>
                <p>Trägt zur Regulierung von Entzündungsprozessen bei regelmäßiger Belastung bei.</p>
            </div>
            """, unsafe_allow_html=True)

        # 5. Vitamin D3
        if wenig_sonne:
            st.markdown("""
            <div class="dashboard-card">
                <h4>☀️ Vitamin D3 + K2 <span class="target-value">Zielwert: 1 Dosis</span></h4>
                <p><b>Anwendung:</b> Jeden zweiten Tag zu einer fetthaltigen Mahlzeit.</p>
                <p>Kompensiert die geringe körpereigene Synthese durch fehlendes Sonnenlicht.</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# BEREICH 2: DAS DETAIL-LEXIKON (Zum Nachschlagen)
# ==========================================
st.subheader("🔍 INHALTSSTOFFE NACHSCHLAGEN")

with st.expander("📖 Übersicht aller Substanzen zum Stöbern öffnen"):
    for name in sorted(list(SUPP_DB.keys())):
        st.markdown(f'<div class="lexicon-box"><b>{name}</b></div>', unsafe_allow_html=True)

auswahl = st.selectbox(
    "Wähle eine Substanz für biochemische Details:", 
    ["Bitte wählen..."] + sorted(list(SUPP_DB.keys()))
)

if auswahl != "Bitte wählen...":
    details = SUPP_DB[auswahl]
    # Dynamisches Icon aus der DB ziehen, falls vorhanden, sonst Standard-DNA
    icon = details.get("icon", "🧬")
    st.markdown(f"""
    <div class="dashboard-card" style="border-top: 3px solid #38BDF8;">
        <h4>{icon} {auswahl}</h4>
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
