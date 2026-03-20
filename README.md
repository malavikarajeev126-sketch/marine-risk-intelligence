<h1>Marine Risk Intelligence Dashboard</h1>

<h2>Overview</h2>
The Marine Risk Intelligence Dashboard is a data-driven system designed to analyze weather conditions along ship routes and assess travel safety.
It combines <b>data analysis, visualization, and risk modeling</b> to help understand how environmental factors like wind speed and wave height impact maritime navigation.

<h2> Key Features</h2>  
- Multi-panel analytical dashboard <br>
- Wave height trend analysis with risk thresholds <br>
- Wind speed monitoring with rolling averages <br>
- Correlation analysis between wind and wave conditions <br>
- Risk classification system: <br>
  - 🟢 Safe <br>
  - 🟠 Moderate<br>
  - 🔴 Dangerous<br>
- Realistic simulated weather dataset (with patterns + noise)<br>
- Time-series + scatter + distribution visualizations<br>
  
<h2> Dashboard Preview</h2>  
![Dashboard](dashboard.png)<br>
---

 <h2>How It Works</h2>
1. Weather data is loaded and cleaned  <br>
2. A **Risk Score** is calculated:<br>
      Risk = Wind Speed × Wave Height<br>
3. Conditions are classified into safety levels<br>  
4. Trends and patterns are visualized using a structured dashboard<br>  

 <h2>Key Insights</h2>
- Wind speed and wave height show a <b>strong positive correlation</b><br>  
- Sudden spikes indicate <b>storm-like conditions</b><br>  
- Majority of days are safe, but  <b>critical high-risk windows exist</b><br>  
- Rolling averages help identify  <b>underlying trends</b><br>

 <h2> Tech Stack </h2>  
- Python<br>
- Pandas<br>
- Matplotlib<br>
- NumPy<br>
---<br>

<h2> Project Structure </h2>  
marine-risk-intelligence/<br>
│<br>
├── data/<br>
│ └── weather_data.csv<br>
├── analysis.py<br>
├── generate_data.py<br>
├── dashboard.png<br>
└── README.md<br>

<h2> Future Enhancements </h2>  
-  Real-time weather API integration  <br>
-  Machine learning-based risk prediction  <br>
-  Interactive web dashboard (Streamlit)  <br>
-  Route optimization for ships  <br>

<h2>👩‍💻 Author </h2>  <br>
<B>Malavika Rajeevan</B> <br>


 ⭐ If you like this project
Give it a ⭐ on GitHub and share your feedback!
