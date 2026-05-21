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
    .stApp {
        background-color: #0F172A; 
        color: #F8FAFC; 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .block-container {
        padding: 2rem 1.2rem !important;
        max-width: 440px !important;
        margin: 0 auto;
    }
    h1 {
        font-size: 2.8rem !important; 
        font-weight: 900 !important; 
        letter-spacing: -1.5px; 
        text-align: center !important; 
        margin-top: 10px !important;
        margin-bottom: 0px !important;
        background: linear-gradient(135deg, #FFFFFF 30%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    h3 {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #F1F5F9 !important; 
        margin-top: 30px !important;
        margin-bottom: 15px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .stNumberInput label, .stSlider label, .stSelectbox label, .stCheckbox p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    .supp-box {
        background: #1E293B;
        border: 1px solid #334155;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-size: 0.9rem;
        color: #F1F5F9;
    }
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
        font-size: 0.88rem;
        color: #E2E8F0; 
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
    .lexicon-box {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 8px;
        font-size: 0.9rem;
        color: #E2E8F0;
    }
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
        text-align: center !important;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(56, 189, 248, 0.3);
    }
    .custom-disclaimer {
        font-size: 0.8rem;
        color: #94A3B8; 
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
# SCIENTIFIC DATABASE (Alle 17 legalen Supplements sind zurück!)
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
        "icon": "🔋",
        "wirkung": "Trägt zur normalen Muskelfunktion und Verringerung von Ermüdung bei.",
        "koerper": "Reguliert als Co-Faktor in über 300 Enzymsystemen die neuronale Erregungsleitung."
    },
    "Zink (Picolinat)": {
        "icon": "🛡️",
        "wirkung": "Essentielles Spurenelement für den Makronährstoff-Stoffwechsel.",
        "koerper": "Unterstützt die zelluläre Eiweißsynthese und die normale Funktion des Immunsystems."
    },
    "L-Citrullin Malat": {
        "icon": "🚀",
        "wirkung": "Wird im Pre-Workout-Bereich zur Unterstützung der Durchblutung genutzt.",
        "koerper": "Fördert die Stickstoffmonoxid-Produktion (NO) im Blut und weitet funktionell die Gefäße."
    },
    "Beta-Alanin": {
        "icon": "🔥",
        "wirkung": "Wird zur Hinauszögerung der Muskelermüdung bei intensiven Sätzen eingesetzt.",
        "koerper": "Erhöht den Carnosingehalt im Muskel, welcher der Übersäuerung durch Milchsäure entgegenwirkt."
    },
    "Ashwagandha (KSM-66)": {
        "icon": "🌿",
        "wirkung": "Pflanzliches Adaptogen zur Unterstützung der Regeneration.",
        "koerper": "Kann helfen, den Cortisolspiegel (Stresshormon) zu regulieren und den Schlaf zu verbessern."
    },
    "Koffein Anhydrous": {
        "icon": "⚡",
        "wirkung": "Temporäre Erhöhung von Fokus, Wachsamkeit und mentaler Energie.",
        "koerper": "Blockiert die Adenosinrezeptoren im Gehirn und verzögert das Müdigkeitssignal."
    },
    "L-Tyrosin": {
        "icon": "🧠",
        "wirkung": "Sorgt für Fokus und Konzentration in extremen Stresssituationen.",
        "koerper": "Dient als Baustein für die Neurotransmitter Dopamin und Adrenalin im Gehirn."
    },
    "Taurin": {
        "icon": "🌊",
        "wirkung": "Unterstützt den Zell-Flüssigkeitshaushalt und zögert Muskelerschöpfung hinaus.",
        "koerper": "Wirkt als Antioxidans und stabilisiert Zellmembranen im Muskelgewebe."
    },
    "Rote Beete Extrakt": {
        "icon": "🩸",
        "wirkung": "Optimiert die Sauerstoffversorgung und die Durchblutung der Muskulatur.",
        "koerper": "Liefert anorganische Nitrate, die im Körper hocheffizient zu Stickstoffmonoxid (NO) umgewandelt werden."
    },
    "EAAs (Aminosäuren)": {
        "icon": "🧱",
        "wirkung": "Verhindert Muskelabbau während des Trainings und startet die Regeneration.",
        "koerper": "Liefert die 9 essenziellen Aminosäuren, die für die Proteinsynthese zwingend benötigt werden."
    },
    "L-Glutamin": {
        "icon": "🩹",
        "wirkung": "Unterstützt das Immunsystem und die Regeneration der Darmgesundheit nach hartem Sport.",
        "koerper": "Dient den Immunzellen und Schleimhautzellen als primäre Energiequelle."
    },
    "MSM (Schwefel)": {
        "icon": "🦴",
        "wirkung": "Unterstützt Gelenke, Sehnen und lindert leichten Muskelkater.",
        "koerper": "Liefert organischen Schwefel, der für die Festigkeit von Bindegewebe und Knorpelstrukturen essenziell ist."
    }
}

# --- APP BRANDING ---
st.markdown('<h1>🧬 ESUP</h1>', unsafe_allow_html=True)
st.markdown('<p translate="no" style="font-size: 1rem; color: #38BDF8; font-weight: 700; text-align: center; margin-top: -5px; margin-bottom: 25px; letter-spacing: 1px; text-transform: uppercase;">Easy Supplements</p>', unsafe_allow_html=True)

# ==========================================
# BEREICH 1: DIE DIAGNOSE-KONSOLE
# ==========================================
st.subheader("⚡ DEIN PROFIL-CHECK")

gewicht = st.number_input("Körpergewicht (kg):", min_value=40, max_value=150, value=80, step=1)
sport_tage = st.slider("Trainingsfrequenz (Tage pro Woche):", 0, 7, 3)

st.markdown("<p style='font-size:0.9rem; font-weight:700; color:#FFFFFF; margin-bottom:5px; margin-top:15px;'>Ernährung & Lifestyle:</p>", unsafe_allow_html=True)
kein_fisch = st.checkbox("Verzicht auf Fischkonsum / Fischallergie")
wenig_sonne = st.checkbox("Geringe Sonnenexposition (< 15 Min. täglich)")
viel_stress = st.checkbox("Ich habe aktuell viel Stress / Schlafprobleme")

st.markdown(" ")
arzt_check = st.checkbox("Ich bestätige, dass diese Berechnung eine unverbindliche Orientierung darstellt.")

if st.button("Unverbindliche Empfehlung berechnen"):
    if not arzt_check:
        st.error("⚠️ Bitte bestätige zuerst die Kenntnisnahme des Hinweises.")
    else:
        st.success("Analyse erfolgreich abgeschlossen.")
        st.markdown("<h3 style='text-align: center;'>📋 DEIN TÄGLICHER ATHLETEN-STACK</h3>", unsafe_allow_html=True)
        
        # 1. Kreatin
        if sport_tage >= 3:
            kr_menge = round(gewicht * 0.05, 1)
            st.markdown(f"""<div class="dashboard-card"><h4>💪 Kreatin Monohydrat <span class="target-value">Zielwert: ca. {kr_menge}g</span></h4><p><b>Anwendung:</b> Täglich direkt nach der Belastung einnehmen.</p><p>Unterstützt die ATP-Resynthese bei deiner Frequenz von {sport_tage} Trainingstagen.</p></div>""", unsafe_allow_html=True)

        # 2. Kollagen
        kol_kapseln = 3 if sport_tage >= 4 else 2
        st.markdown(f"""<div class="dashboard-card"><h4>✨ Gelenk-Kollagen <span class="target-value">Zielwert: ca. {kol_kapseln} Kapseln</span></h4><p><b>Anwendung:</b> Morgens unabhängig von den Mahlzeiten einnehmen.</p><p>Sichert die gezielte Aminosäurenversorgung für Sehnen und Knorpelgewebe.</p></div>""", unsafe_allow_html=True)

        # 3. Whey Protein
        if sport_tage >= 1:
            st.markdown("""<div class="dashboard-card"><h4>🥛 Proteinquelle (Whey) <span class="target-value">Zielwert: 1 Shake (30g)</span></h4><p><b>Anwendung:</b> Unmittelbar nach dem Training oder morgens an spielfreien Tagen.</p><p>Unterstützt die Muskelproteinsynthese bei sportlich erhöhtem Bedarf.</p></div>""", unsafe_allow_html=True)

        # 4. Omega-3 Logik
        if kein_fisch:
            st.markdown("""<div class="dashboard-card"><h4>🌱 Veganes Algenöl <span class="target-value">Zielwert: 2 Kapseln</span></h4><p><b>Anwendung:</b> Zu einer fetthaltigen Hauptmahlzeit einnehmen.</p><p>Pflanzliche Absicherung der essenziellen EPA/DHA-Werte bei Fischverzicht.</p></div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="dashboard-card"><h4>🐟 Omega-3 Fischöl <span class="target-value">Zielwert: 1 Kapsel</span></h4><p><b>Anwendung:</b> Zu einer beliebigen Mahlzeit einnehmen.</p><p>Trägt zur Regulierung von Entzündungsprozessen bei regelmäßiger Belastung bei.</p></div>""", unsafe_allow_html=True)

        # 5. Vitamin D3
        if wenig_sonne:
            st.markdown("""<div class="dashboard-card"><h4>☀️ Vitamin D3 + K2 <span class="target-value">Zielwert: 1 Dosis</span></h4><p><b>Anwendung:</b> Jeden zweiten Tag zu einer fetthaltigen Mahlzeit.</p><p>Kompensiert die geringe körpereigene Synthese durch fehlendes Sonnenlicht.</p></div>""", unsafe_allow_html=True)

        # 6. Regeneration Basics bei viel Sport (Magnesium, Zink, MSM, Glutamin)
        if sport_tage >= 4:
            st.markdown("""<div class="dashboard-card"><h4>🔋 Regeneration & Gelenke (Magnesium, Zink, MSM, Glutamin) <span class="target-value">Zielwert: Basis-Dosis</span></h4><p><b>Anwendung:</b> Magnesium und Glutamin vor dem Schlafen einnehmen.</p><p>Fördert die ZNS-Regeneration und schützt stark beanspruchte Gelenk- und Muskelstrukturen.</p></div>""", unsafe_allow_html=True)

        # 7. Pre-Workout Booster (Citrullin, Beta-Alanin, Coffein, Tyrosin, Taurin, Rote Beete)
        if sport_tage >= 4:
            st.markdown("""<div class="dashboard-card"><h4>🚀 Fokus & Pump Matrix (Pre-Workout Allrounder) <span class="target-value">Zielwert: Vor dem Training</span></h4><p><b>Anwendung:</b> Ca. 30–45 Minuten vor harten Einheiten auf leeren Magen konsumieren.</p><p>Optimiert die Durchblutung (Stickstoffmonoxid) und schärft den mentalen Fokus unter Belastung.</p></div>""", unsafe_allow_html=True)

        # 8. Ashwagandha Logik
        if viel_stress:
            st.markdown("""<div class="dashboard-card"><h4>🌿 Ashwagandha (KSM-66) <span class="target-value">Zielwert: 1 Kapsel</span></h4><p><b>Anwendung:</b> Abends vor dem Schlafen einnehmen.</p><p>Unterstützt den Organismus bei der Regulierung des Cortisolspiegels (Stresshormon).</p></div>""", unsafe_allow_html=True)

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
