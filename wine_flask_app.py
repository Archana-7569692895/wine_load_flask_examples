from flask import Flask, request
import joblib


# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)


# =========================================================
# LOAD MODEL
# =========================================================

classifier = joblib.load("lr_wine_load.pkl")


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>WineIQ | Wine Quality Prediction</title>


<style>

/* =====================================================
   BASIC
===================================================== */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {

    font-family: Arial, Helvetica, sans-serif;

    color: white;

    min-height: 100vh;

    background:
        radial-gradient(
            circle at 85% 20%,
            #b51d70 0%,
            transparent 22%
        ),

        radial-gradient(
            circle at 10% 70%,
            #65238c 0%,
            transparent 25%
        ),

        radial-gradient(
            circle at 75% 90%,
            #b54b18 0%,
            transparent 25%
        ),

        linear-gradient(
            135deg,
            #17030e,
            #350920,
            #570b36,
            #270b42,
            #10020b
        );

    overflow-x: hidden;
}


/* =====================================================
   NAVBAR
===================================================== */

nav {

    height: 82px;

    padding: 0 7%;

    display: flex;

    align-items: center;

    justify-content: space-between;

    position: sticky;

    top: 0;

    z-index: 100;

    background:
        rgba(25, 2, 15, 0.90);

    backdrop-filter: blur(15px);

    border-bottom:
        1px solid
        rgba(255,255,255,0.12);
}


.logo {

    display: flex;

    align-items: center;

    gap: 10px;

    font-size: 28px;

    font-weight: bold;
}


.logo-icon {

    width: 43px;

    height: 43px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #ff1680,
            #ff9d00
        );

    box-shadow:
        0 0 25px
        rgba(255,50,140,0.5);
}


.logo span {

    background:
        linear-gradient(
            90deg,
            #ff5b9c,
            #ffd166,
            #ff9d00
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}


nav ul {

    display: flex;

    gap: 35px;

    list-style: none;
}


nav ul a {

    color: #f5dce8;

    text-decoration: none;

    transition: 0.3s;
}


nav ul a:hover {

    color: #ff6fa5;
}


/* =====================================================
   HERO
===================================================== */

.hero {

    min-height: 650px;

    padding:
        70px 7%;

    display: flex;

    align-items: center;

    justify-content: space-between;

    position: relative;
}


.hero-left {

    width: 55%;

    z-index: 5;
}


.badge {

    display: inline-block;

    padding:
        11px 18px;

    border-radius: 30px;

    color: #ffd166;

    background:
        linear-gradient(
            90deg,
            rgba(255,40,125,0.20),
            rgba(255,170,30,0.18)
        );

    border:
        1px solid
        rgba(255,150,190,0.35);

    margin-bottom: 28px;
}


h1 {

    font-family: Georgia, serif;

    font-size: 70px;

    line-height: 1.02;

    margin-bottom: 25px;
}


.white {

    color: white;
}


.pink {

    background:
        linear-gradient(
            90deg,
            #ff559c,
            #ff9e3d,
            #ffd166
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}


.purple {

    background:
        linear-gradient(
            90deg,
            #d77cff,
            #ff61b0
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}


.description {

    max-width: 600px;

    color: #e2c6d5;

    font-size: 18px;

    line-height: 1.7;

    margin-bottom: 30px;
}


.start-btn {

    display: inline-block;

    padding:
        15px 27px;

    border-radius: 14px;

    color: white;

    text-decoration: none;

    font-weight: bold;

    background:
        linear-gradient(
            135deg,
            #ff1672,
            #ff5935,
            #ffad1f
        );

    box-shadow:
        0 10px 35px
        rgba(255,40,110,0.4);

    transition: 0.3s;
}


.start-btn:hover {

    transform:
        translateY(-4px);

    box-shadow:
        0 15px 45px
        rgba(255,40,110,0.6);
}


/* =====================================================
   WINE VISUAL
===================================================== */

.hero-right {

    width: 42%;

    height: 470px;

    position: relative;

    display: flex;

    align-items: center;

    justify-content: center;
}


.wine-glow {

    position: absolute;

    width: 430px;

    height: 430px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(255,35,130,0.38),
            rgba(130,40,255,0.18),
            transparent 70%
        );

    filter: blur(8px);
}


/* =====================================================
   WINE GLASS
===================================================== */

.wine-glass {

    position: relative;

    z-index: 5;

    width: 220px;

    animation:
        floatWine 4s ease-in-out infinite;
}


.glass {

    width: 205px;

    height: 210px;

    position: relative;

    overflow: hidden;

    border:
        7px solid
        rgba(240,250,255,0.72);

    border-top-left-radius: 45%;

    border-top-right-radius: 45%;

    border-bottom-left-radius: 50%;

    border-bottom-right-radius: 50%;

    background:
        rgba(255,255,255,0.08);

    box-shadow:
        0 0 30px
        rgba(255,255,255,0.15);
}


.wine {

    position: absolute;

    bottom: 0;

    left: 0;

    width: 100%;

    height: 58%;

    background:
        linear-gradient(
            180deg,
            #ff43ae,
            #c50070,
            #690035
        );

    border-radius:
        0 0 45% 45%;
}


.stem {

    width: 9px;

    height: 95px;

    margin:
        -3px auto 0;

    background:
        linear-gradient(
            90deg,
            white,
            #aeeaff,
            white
        );
}


.base {

    width: 115px;

    height: 10px;

    margin: auto;

    border-radius: 50%;

    background:
        linear-gradient(
            90deg,
            white,
            #aeeaff,
            white
        );
}


@keyframes floatWine {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-18px);
    }
}


/* =====================================================
   WINE BOTTLE
===================================================== */

.bottle {

    position: absolute;

    right: 10px;

    bottom: 45px;

    width: 105px;

    height: 280px;

    z-index: 3;

    transform: rotate(5deg);

    filter:
        drop-shadow(
            0 20px 20px
            rgba(0,0,0,0.5)
        );
}


.bottle-neck {

    width: 42px;

    height: 90px;

    margin: auto;

    background:
        linear-gradient(
            90deg,
            #280315,
            #8d173e,
            #3b061f
        );

    border-radius:
        8px 8px 0 0;
}


.bottle-body {

    width: 105px;

    height: 190px;

    background:
        linear-gradient(
            90deg,
            #240315,
            #791039,
            #b72c61,
            #35051d
        );

    border-radius:
        25px 25px 35px 35px;

    position: relative;
}


.bottle-label {

    position: absolute;

    width: 70px;

    height: 80px;

    top: 65px;

    left: 17px;

    display: flex;

    justify-content: center;

    align-items: center;

    text-align: center;

    border-radius: 8px;

    background:
        linear-gradient(
            135deg,
            #ffd166,
            #fff1b8
        );

    color: #5c0926;

    font-family: Georgia, serif;

    font-weight: bold;

    font-size: 12px;
}


/* =====================================================
   FLOATING CARDS
===================================================== */

.info-card {

    position: absolute;

    z-index: 10;

    display: flex;

    align-items: center;

    gap: 10px;

    padding:
        13px 17px;

    border-radius: 16px;

    background:
        rgba(25,3,18,0.80);

    backdrop-filter: blur(15px);

    border:
        1px solid
        rgba(255,255,255,0.15);

    box-shadow:
        0 15px 40px
        rgba(0,0,0,0.3);
}


.card-one {

    top: 45px;

    right: 0;
}


.card-two {

    bottom: 50px;

    left: 0;
}


.card-icon {

    width: 42px;

    height: 42px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            #ff187d,
            #9d4edd
        );
}


.info-card strong {

    display: block;
}


.info-card small {

    color: #cdb1c2;
}


/* =====================================================
   WINE DATA
===================================================== */

.data-section {

    padding:
        70px 7%;
}


.title {

    text-align: center;

    margin-bottom: 40px;
}


.title h2 {

    font-family: Georgia, serif;

    font-size: 42px;

    margin-bottom: 10px;
}


.title p {

    color: #d3b5c5;
}


.data-grid {

    display: grid;

    grid-template-columns:
        repeat(4,1fr);

    gap: 18px;
}


.data-card {

    padding: 25px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.10),
            rgba(255,255,255,0.035)
        );

    border:
        1px solid
        rgba(255,255,255,0.12);

    transition: 0.3s;
}


.data-card:hover {

    transform:
        translateY(-8px);

    border-color:
        rgba(255,90,150,0.5);
}


.data-icon {

    font-size: 32px;

    margin-bottom: 12px;
}


.data-card h3 {

    margin-bottom: 8px;
}


.data-card p {

    color: #c9aebc;

    line-height: 1.5;

    font-size: 14px;
}


/* =====================================================
   PREDICTION
===================================================== */

.prediction-section {

    padding:
        80px 7%;
}


.prediction-box {

    max-width: 1050px;

    margin: auto;

    padding: 40px;

    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(255,35,120,0.14),
            rgba(120,40,255,0.13),
            rgba(255,150,30,0.12)
        );

    border:
        1px solid
        rgba(255,255,255,0.16);

    box-shadow:
        0 25px 80px
        rgba(0,0,0,0.3);
}


.prediction-box h2 {

    text-align: center;

    font-family: Georgia, serif;

    font-size: 40px;

    margin-bottom: 10px;
}


.prediction-box > p {

    text-align: center;

    color: #d4b7c6;

    margin-bottom: 30px;
}


.form-grid {

    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 17px;
}


.input-box {

    display: flex;

    flex-direction: column;
}


.input-box label {

    font-size: 13px;

    color: #e6cad7;

    margin-bottom: 7px;
}


.input-box input {

    padding: 13px;

    border-radius: 11px;

    border:
        1px solid
        rgba(255,255,255,0.15);

    background:
        rgba(0,0,0,0.25);

    color: white;

    outline: none;
}


.input-box input:focus {

    border-color: #ff599d;

    box-shadow:
        0 0 15px
        rgba(255,80,150,0.15);
}


.predict-btn {

    width: 100%;

    padding: 17px;

    margin-top: 25px;

    border: none;

    border-radius: 13px;

    color: white;

    font-size: 17px;

    font-weight: bold;

    cursor: pointer;

    background:
        linear-gradient(
            90deg,
            #ff1674,
            #ff5935,
            #ffad1f,
            #c13cff
        );

    transition: 0.3s;
}


.predict-btn:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0 10px 30px
        rgba(255,50,120,0.35);
}


#result {

    margin-top: 20px;

    padding: 20px;

    text-align: center;

    border-radius: 15px;

    background:
        rgba(0,0,0,0.25);

    color: #ffd166;

    font-size: 21px;

    font-weight: bold;
}


/* =====================================================
   FOOTER
===================================================== */

footer {

    padding: 30px;

    text-align: center;

    color: #a98b9c;

    border-top:
        1px solid
        rgba(255,255,255,0.1);
}


footer span {

    color: #ff659e;
}


/* =====================================================
   RESPONSIVE
===================================================== */

@media(max-width:900px) {

    nav ul {
        display: none;
    }

    .hero {

        flex-direction: column;

        text-align: center;
    }

    .hero-left,
    .hero-right {

        width: 100%;
    }

    .hero-right {

        margin-top: 50px;
    }

    h1 {

        font-size: 50px;
    }

    .description {

        margin-left: auto;

        margin-right: auto;
    }

    .data-grid {

        grid-template-columns:
            repeat(2,1fr);
    }

    .form-grid {

        grid-template-columns: 1fr;
    }
}


@media(max-width:600px) {

    .data-grid {

        grid-template-columns: 1fr;
    }

}

</style>

</head>


<body>


<!-- =====================================================
     NAVBAR
===================================================== -->

<nav>

    <div class="logo">

        <div class="logo-icon">
            🍷
        </div>

        Wine<span>IQ</span>

    </div>


    <ul>

        <li>
            <a href="#home">Home</a>
        </li>

        <li>
            <a href="#wine-data">Wine Data</a>
        </li>

        <li>
            <a href="#predict">Predict</a>
        </li>

    </ul>

</nav>



<!-- =====================================================
     HERO
===================================================== -->

<section
    class="hero"
    id="home"
>


    <div class="hero-left">


        <div class="badge">

            ✨ AI Powered Wine Quality Analysis

        </div>


        <h1>

            <span class="white">
                Discover the
            </span>

            <br>

            <span class="pink">
                Quality
            </span>

            <br>

            <span class="purple">
                of Your Wine
            </span>

        </h1>


        <p class="description">

            Analyze the chemical properties of your
            wine using Machine Learning and discover
            its predicted quality score instantly.

        </p>


        <a
            href="#predict"
            class="start-btn"
        >

            🍷 Start Wine Analysis →

        </a>


    </div>



    <!-- =================================================
         WINE GLASS + BOTTLE
    ================================================= -->

    <div class="hero-right">


        <div class="wine-glow"></div>


        <!-- BOTTLE -->

        <div class="bottle">

            <div class="bottle-neck"></div>

            <div class="bottle-body">

                <div class="bottle-label">

                    WINE<br>
                    QUALITY<br>
                    2026

                </div>

            </div>

        </div>


        <!-- GLASS -->

        <div class="wine-glass">

            <div class="glass">

                <div class="wine"></div>

            </div>

            <div class="stem"></div>

            <div class="base"></div>

        </div>


        <!-- FEATURE CARD -->

        <div class="info-card card-one">

            <div class="card-icon">
                🧪
            </div>

            <div>

                <strong>
                    11+
                </strong>

                <small>
                    Wine Features
                </small>

            </div>

        </div>


        <!-- AI CARD -->

        <div class="info-card card-two">

            <div class="card-icon">
                🤖
            </div>

            <div>

                <strong>
                    AI Model
                </strong>

                <small>
                    Quality Prediction
                </small>

            </div>

        </div>


    </div>

</section>



<!-- =====================================================
     WINE DATA
===================================================== -->

<section
    class="data-section"
    id="wine-data"
>


    <div class="title">

        <h2>
            🍷 Wine Quality Data
        </h2>

        <p>
            Chemical properties used by our Machine Learning model
        </p>

    </div>


    <div class="data-grid">


        <div class="data-card">

            <div class="data-icon">🧪</div>

            <h3>
                Fixed Acidity
            </h3>

            <p>
                Important acids that affect
                wine taste and structure.
            </p>

        </div>


        <div class="data-card">

            <div class="data-icon">🍋</div>

            <h3>
                Volatile Acidity
            </h3>

            <p>
                Influences aroma and
                freshness of wine.
            </p>

        </div>


        <div class="data-card">

            <div class="data-icon">🍬</div>

            <h3>
                Residual Sugar
            </h3>

            <p>
                Amount of sugar remaining
                after fermentation.
            </p>

        </div>


        <div class="data-card">

            <div class="data-icon">💧</div>

            <h3>
                Density
            </h3>

            <p>
                Physical characteristic
                of the wine.
            </p>

        </div>


        <div class="data-card">

            <div class="data-icon">⚗️</div>

            <h3>
                pH
            </h3>

            <p>
                Indicates the acidity level
                of the wine.
            </p>

        </div>


        <div class="data-card">

            <div class="data-icon">🍷</div>

            <h3>
                Alcohol
            </h3>

            <p>
                Alcohol percentage is an
                important quality feature.
            </p>

        </div>


        <div class="data-card">

            <div class="data-icon">✨</div>

            <h3>
                Sulphates
            </h3>

            <p>
                Helps with wine preservation
                and stability.
            </p>

        </div>


        <div class="data-card">

            <div class="data-icon">🫧</div>

            <h3>
                Sulfur Dioxide
            </h3>

            <p>
                Important chemical property
                used during wine production.
            </p>

        </div>


    </div>

</section>



<!-- =====================================================
     PREDICTION FORM
===================================================== -->

<section
    class="prediction-section"
    id="predict"
>


    <div class="prediction-box">


        <h2>
            🍷 Predict Your Wine Quality
        </h2>


        <p>
            Enter the 11 wine characteristics
        </p>


        <div class="form-grid">


            <div class="input-box">

                <label>
                    Fixed Acidity
                </label>

                <input
                    id="fixed_acidity"
                    type="number"
                    step="any"
                    placeholder="7.4"
                >

            </div>


            <div class="input-box">

                <label>
                    Volatile Acidity
                </label>

                <input
                    id="volatile_acidity"
                    type="number"
                    step="any"
                    placeholder="0.70"
                >

            </div>


            <div class="input-box">

                <label>
                    Citric Acid
                </label>

                <input
                    id="citric_acid"
                    type="number"
                    step="any"
                    placeholder="0.00"
                >

            </div>


            <div class="input-box">

                <label>
                    Residual Sugar
                </label>

                <input
                    id="residual_sugar"
                    type="number"
                    step="any"
                    placeholder="1.9"
                >

            </div>


            <div class="input-box">

                <label>
                    Chlorides
                </label>

                <input
                    id="chlorides"
                    type="number"
                    step="any"
                    placeholder="0.076"
                >

            </div>


            <div class="input-box">

                <label>
                    Free Sulfur Dioxide
                </label>

                <input
                    id="free_sulfur_dioxide"
                    type="number"
                    step="any"
                    placeholder="11"
                >

            </div>


            <div class="input-box">

                <label>
                    Total Sulfur Dioxide
                </label>

                <input
                    id="total_sulfur_dioxide"
                    type="number"
                    step="any"
                    placeholder="34"
                >

            </div>


            <div class="input-box">

                <label>
                    Density
                </label>

                <input
                    id="density"
                    type="number"
                    step="any"
                    placeholder="0.9978"
                >

            </div>


            <div class="input-box">

                <label>
                    pH
                </label>

                <input
                    id="ph"
                    type="number"
                    step="any"
                    placeholder="3.51"
                >

            </div>


            <div class="input-box">

                <label>
                    Sulphates
                </label>

                <input
                    id="sulphates"
                    type="number"
                    step="any"
                    placeholder="0.56"
                >

            </div>


            <div class="input-box">

                <label>
                    Alcohol
                </label>

                <input
                    id="alcohol"
                    type="number"
                    step="any"
                    placeholder="9.4"
                >

            </div>


        </div>


        <button
            class="predict-btn"
            onclick="predictWine()"
        >

            🍷 ANALYZE WINE QUALITY

        </button>


        <div id="result">

            🍷 Your Wine Quality will appear here

        </div>


    </div>

</section>



<!-- =====================================================
     FOOTER
===================================================== -->

<footer>

    🍷 Wine<span>IQ</span>

    &nbsp; | &nbsp;

    AI Powered Wine Quality Prediction

</footer>



<!-- =====================================================
     JAVASCRIPT
===================================================== -->

<script>

async function predictWine() {


    const fields = [

        "fixed_acidity",
        "volatile_acidity",
        "citric_acid",
        "residual_sugar",
        "chlorides",
        "free_sulfur_dioxide",
        "total_sulfur_dioxide",
        "density",
        "ph",
        "sulphates",
        "alcohol"

    ];


    const values = {};


    for (const field of fields) {

        values[field] =
            document.getElementById(field).value;


        if (values[field] === "") {

            document.getElementById("result").innerHTML =
                "⚠️ Please enter all wine values.";

            return;
        }

    }


    document.getElementById("result").innerHTML =
        "🍷 Analyzing your wine...";


    try {


        const params =
            new URLSearchParams(values);


        const response =
            await fetch(
                "/predict?" +
                params.toString()
            );


        const data =
            await response.json();


        if (data.prediction !== undefined) {

            document.getElementById("result").innerHTML =

                "🍷 Predicted Wine Quality: " +

                Number(data.prediction).toFixed(2) +

                " ⭐";

        }

        else {

            document.getElementById("result").innerHTML =
                "❌ Prediction failed.";

        }


    }

    catch(error) {

        console.log(error);

        document.getElementById("result").innerHTML =
            "❌ Unable to connect to prediction API.";

    }

}

</script>


</body>
</html>
"""


# =========================================================
# PREDICTION ROUTE
# =========================================================

@app.route("/predict")
def predict():

    fixed_acidity = float(
        request.args.get("fixed_acidity")
    )

    volatile_acidity = float(
        request.args.get("volatile_acidity")
    )

    citric_acid = float(
        request.args.get("citric_acid")
    )

    residual_sugar = float(
        request.args.get("residual_sugar")
    )

    chlorides = float(
        request.args.get("chlorides")
    )

    free_sulfur_dioxide = float(
        request.args.get("free_sulfur_dioxide")
    )

    total_sulfur_dioxide = float(
        request.args.get("total_sulfur_dioxide")
    )

    density = float(
        request.args.get("density")
    )

    ph = float(
        request.args.get("ph")
    )

    sulphates = float(
        request.args.get("sulphates")
    )

    alcohol = float(
        request.args.get("alcohol")
    )


    # Put values in SAME ORDER
    # used during model training

    input_data = [[

        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        ph,
        sulphates,
        alcohol

    ]]


    # Prediction

    prediction = classifier["model"].predict(
        input_data
    )


    return {

        "prediction":
            float(prediction[0])

    }


# =========================================================
# RUN FLASK
# =========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )