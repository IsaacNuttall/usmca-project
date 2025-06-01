import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="NAFTA vs USMCA Full Report", layout="wide")

st.title("NAFTA vs USMCA: Full State-Level Impact Analysis")

# Introduction
st.markdown("""
This Streamlit app serves as the full public version of my written analysis and visual data project comparing the socioeconomic impact of the USMCA, and to a lesser extent NAFTA, on each U.S. state. It includes every paragraph, chart, and conclusion from my report, now hosted for interactive access.
""")

st.markdown("""
---

### Introduction
""")

st.markdown("Over the last several decades, globalization has created a seismic shift in economies worldwide. The historic trade agreements of NAFTA and the USMCA stood at the vanguard of this economic realignment, creating vastly different outcomes not only for countries overall but also for individual U.S. states.")

st.markdown("This paper shall analyze the comparative socioeconomic impact of the USMCA, and to a lesser extent NAFTA, on each U.S. state using nine key annual metrics: real GDP, inflation rate, CPI Proxy, immigration to and from Mexico, imports from Mexico, exports to Mexico, trade balance with Mexico, business formations, and job growth.")

st.markdown("The only one of these metrics for which I found pre-1994 data was job growth. Thus, most of this paper’s analysis shall focus on the socioeconomic impact of the USMCA on each U.S. state, with job growth serving as the only variable to evaluate the impact of both NAFTA and the USMCA.")

st.markdown("The data analysis of this paper shall begin by examining which states experienced the greatest impact from the USMCA and, to a lesser extent, NAFTA. This paper will compute this by using an interrupted time series (ITS) regression to show which states experienced a statistically significant change in nine aforementioned variables, with statistically significant defined as having a p-value of less than 0.05.")

st.markdown("Since the ITS regression only returned one state for Mexican migration, this paper will use a two-sample T-test to evaluate statistically significant change in this variable. Then, this paper shall address the states that did not experience a statistically significant change across any of the nine variables after NAFTA or the USMCA. To explain the findings of this data, this paper shall offer hypotheses and qualitative data at each step of data analysis.")

# Methodology
st.markdown("""
---

### Methodology
""")

st.markdown("To prepare each of the nine aforementioned variables for analysis, I engaged in extensive data cleaning and mathematical transformations. I performed my data analysis using a Jupyter notebook, created a SQL database, and coded in Python and its associated libraries, most notably pandas.")

st.markdown("Using data from the U.S. Bureau of Economic Analysis, I obtained statewide data from 1997 to 2023 for real GDP (millions of chained 2017 USD) and nominal GDP (millions of current USD). When I analyze the impact of the USMCA on statewide GDP later in this paper, I will use real GDP since this provides a value adjusted for inflation.")

st.markdown("However, I used both real GDP and nominal GDP to calculate the annual inflation rate for each state. I did this by calculating the GDP deflator (nominal GDP divided by real GDP, then multiplied by 100), and then calculating the annual inflation rate as the percent change in GDP deflator, multiplied by 100 again.")

st.markdown("To gain additional insight into how the USMCA has impacted consumer spending and saving habits, I divided real per-capita personal consumption by real per-capita personal income to obtain a proxy value for CPI since I could not find official statewide CPI data from 2008 to 2023.")

st.markdown("I obtained this data from the U.S. Bureau of Economic Analysis. The CPI proxy value complements the annual inflation rate since it illustrates the extent to which consumers spend relative to their income, with a higher value indicating more consumer spending and a lower value indicating less.")

st.markdown("In addition to the economic sphere, the USMCA had profound social impacts, most notably on immigration. I obtained data from the ACS 5-Year Survey from 2010 to 2023 using the United States Census API to quantify this.")

st.markdown("Then, I calculated the annual percentage of a state’s population born in Mexico by dividing the Mexican-born population of a state by its total population and multiplying the result by 100. For any states that had missing values for certain years, I filled these values using interpolation, a method that estimates values using known data points.")

st.markdown("Thus, this paper shall define a state’s Mexican immigration rate as the change in its population born in Mexico.")

st.markdown("For trade, arguably the most critical economic variable to analyze, I obtained annual statewide data from the U.S. International Trade Administration (in millions of USD) from 2009 to 2024 on imports from Mexico, exports to Mexico, and subtracted annual imports from exports to calculate each state’s trade balance with Mexico.")

st.markdown("Then, I computed business formations by obtaining annual, seasonally-adjusted data from the Federal Reserve Bank of Saint Louis on statewide spliced business formations, with an observation date of January first of each year.")

st.markdown("Some states had annual data for spliced business formations within eight quarters, while others had this data within four quarters. To standardize this data, I divided each state’s dataset by eight or four, depending on the number of quarters in which the data was obtained.")

st.markdown("Thus, this paper shall utilize annual data on spliced business formations per quarter.")

st.markdown("Finally, I garnered annual data from the Arizona State University Seidman Institute, sourced from the U.S. Bureau of Labor Statistics, on the annual percent change of jobs in the U.S. from 1990 to 2024.")

# Key Findings Heading
st.markdown("""
---

### Key Findings with Visuals
""")

# Display function
def display_section(title, image_file, *explanation_parts):
    st.header(title)
    image_path = os.path.join("images", image_file)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=title, use_container_width=True)
    else:
        st.warning(f"Image not found: {image_path}")
    
    for paragraph in explanation_parts:
        st.markdown(paragraph)

# List of sections (partial example; add remaining as needed)
visuals = [
    (
        "Real GDP Impact",
        "GDP_Impact_Image_2025.png",
        "Idaho, Arizona, and Maine all experienced a positive, statistically significant change in real GDP following the implementation of the USMCA. Real estate and rental leasing is the biggest industry of all three states.",
        "Thus, the USMCA most likely bolstered the economies of all three states due to the USMCA’s new provisions surrounding e-commerce, data flows, and data localization, which have formed a core pillar of the success of the industrial real estate sector.",
        "Specifically, the USMCA introduced new provisions on digital trade, such as prohibiting customs duties on electronically transmitted products and protecting cross-border data flows. The USMCA digital trade chapter also includes more advanced provisions that prohibit data localization policies and limit source code disclosure requirements.",
        "These provisions likely benefitted the industrial real estate sector, whose growth has been “largely driven by e-commerce growth and increased demand for logistics hubs,” by bolstering businesses that rely on digital services, such as Airbnb and Zillow.",
        "This makes short-term rentals and cross-border real estate investments more efficient, especially for states that border Canada, such as Idaho and Maine, since “Canadian firms, pension funds, and private investors have historically been among the largest foreign buyers of American office buildings, retail centers, and industrial properties.”",
        "Idaho, with its large dairy industry, also stood to gain from the USMCA’s provision giving the United States increased access to the Canadian dairy market.",
        "Specifically, U.S. milk, cheese, cream, skim milk powder, condensed milk, yogurt, and several other dairy categories received expanded access to Canada. In return, the United States expanded import quota levels for Canadian dairy and sugar products.",
        "Additionally, the USMCA’s enhanced protections surrounding intellectual property rights, such as the inclusion of criminal and civil penalties for trade secret theft and cyber-theft, likely increased foreign investor confidence in the U.S. real estate market."
    ),
    (
        "Inflation Impact", 
        "Inflation_Impact_Image_2025.png", 
        "Idaho and Nebraska both experienced a statistically significant inflation increase following the implementation of the USMCA. Real estate and rental leasing form the biggest industry in Idaho, and manufacturing forms the biggest industry in Nebraska.",
        "Since Idaho saw a statistically significant increase in inflation but not CPI proxy, consumers likely had a sufficient increase in income to withstand inflation, a notion further supported by Idaho’s statistically significant increase in real GDP.",
        "Nebraska, however, with an economy reliant on manufacturing, likely saw an increase in inflation due to the USMCA’s stricter requirements surrounding the sourcing of auto parts from North America, increased wage requirements, and stronger labor protections, which directly impact consumer prices."
    ),
    (
        "CPI Proxy Impact", 
        "CPI_Proxy_Impact_Image_2025.png", 
        "Just as inflation rose for all U.S. states following the USMCA, the CPI Proxy value fell for all U.S. states, meaning that consumers spent less relative to their income.", 
        "However, 15 states saw a particularly large, statistically significant drop. Manufacturing is the main industry for 60% of these states, including Nebraska, Minnesota, Iowa, Missouri, Arkansas, Louisiana, Michigan, Kentucky, and Alabama. Mining, quarrying, and oil and gas extraction account for an additional 20%, including New Mexico, North  Dakota, and West Virginia.", 
        "The USMCA’s enhanced provisions on labor and the environment, additional requirements on auto parts sourced in North America, and elimination of NAFTA’s energy chapter likely played a major role in this, raising the cost of manufacturing and energy and passing the price on to consumers. Consumers, in turn, likely spent less money relative to their income, as shown by the reduction in the CPI Proxy value."
    ),
    (
        "Net Migration from Mexico Impact", 
        "Net_Migration_Impact_Image_2025.png", 
        "Based on a two-sample T-test, four states saw a statistically significant change in Mexican immigration, calculated as the percentage of a state’s population born in Mexico.",
        "Rhode Island, which primarily relies on real estate and rental leasing, likely relies more on raw materials and construction, as hypothesized in the previous paragraph. This likely served as a pull factor for migrants, who make up a large share of the construction workforce.",
        "However, the real estate and rental industries of Montana and Vermont likely focus more on services, which the USMCA did not address as thoroughly, dissuading potential migration.", 
        "Additionally, Rhode Island is primarily controlled by the Democratic party, while Montana and Wyoming are primarily controlled by the Republican party, which is more hostile to immigrants. This likely created an additional push factor against Mexican immigration to Montana and Wyoming."
    ),
    (
        "Import Impact", 
        "Import_Impact_Image_2025.png", 
        "The USMCA resulted in a significant change in the Mexican imports of 14 states, with a roughly even effect.",
        "The states that gained imports, including Minnesota, New Mexico, Louisiana, Mississippi, Georgia, Maryland, and Maine, primarily rely on manufacturing, real estate and rental leasing, mining, quarrying, and oil and gas extraction. Imports from Mexico likely increased for these states due to the USMCA’s strengthening of regional supply chains and reduced costs for items such as construction materials, manufacturing inputs, and energy.", 
        "States that saw a reduction in Mexican imports, such as Washington, New York, Montana, Colorado, and Rhode Island, rely more on services such as information, real estate and rental leasing, and finance and insurance. Since the USMCA does not place as great an emphasis on services, these states likely found new trading partners or sourced more services within their borders."
    ),
    (
        "Export Impact", 
        "Export_Impact_Image_2025.png", 
        "The USMCA resulted in a significant change in the Mexican exports of 14 states, with a mostly negative effect.",
        "Hawaii, Nevada, and Montana, whose economies primarily rely on real estate and rental leasing, likely benefited from the USMCA’s new provisions on e-commerce, data flows, and general strengthening of regional supply chains, allowing them to export additional goods and services to Mexico.", 
        "Specifically, the new USMCA provisions, such as prohibiting customs duties on electronically transmitted products and protecting cross-border data flows, created a more favorable environment for businesses that rely on digital services such as apartments.com and realtor.com. As Forbes explained, “Technology is bridging the gap between people and properties by offering much-needed solutions, including connecting companies to their remote workers, streamlining property marketing and property management operations, and collecting data to help us better understand the market and be prepared for economic downturns.”",
        "Data from the U.S. International Trade Administration also finds that Nevada saw significant export gains in computer and electronic products following the implementation of the USMCA. This further supports the notion that technology has formed a fundamental pillar of economic growth for real estate-dominant states and elsewhere.",
        "Wyoming’s increase in exports almost entirely came from basic chemicals, likely benefiting from the USMCA’s measures to harmonize chemical regulations across the U.S., Canada, and Mexico, including the “respective implementation of the United Nations Globally Harmonized System for Classification and Labeling of Chemicals (GHS).”", 
        "Most states that saw a significant reduction in exports to Mexico, including Minnesota, Wisconsin, Illinois, Indiana, Ohio, Louisiana, and South Carolina, have economies primarily reliant on manufacturing.", 
        "This likely suggests that the USMCA’s new provisions, such as requiring new motor vehicles to have at least 75% of their content sourced in North America, requiring that 40-45% of auto content be made by workers earning at least $16 an hour, and “rapid response” mechanism designed to bolster workers’ rights in Mexico did not make the U.S. manufacturing industry more competitive. These provisions may have done the opposite, increasing manufacturing costs so much that it became untenable to do business.", 
        "The USMCA’s rule of origin requirement likely dealt an especially strong blow to Ohio and Indiana since both states have large auto sectors focusing more on parts than vehicle manufacturing. As a result, manufacturers in these states faced higher costs as they could source fewer of their materials outside North America.", 
        "Aside from manufacturing states, the real-estate-reliant states of Arizona and Rhode Island also suffered export losses to Mexico, contrasting with the gains of real-estate-reliant Hawaii, Nevada, and Rhode Island.", 
        "For Rhode Island, this was most likely because, according to Forbes:\n```\nRhode Island’s real estate and rental and leasing industry has not fared well over the years, declining by 9.6% from fourth quarter 2011 ($8.22 billion) to fourth quarter 2021 ($7.43 billion).\n```", 
        "Thus, despite Arizona’s strong real estate industry, the state’s border with Mexico allowed Mexican maquiladoras (factories right across the border) to benefit from increased cross-border trade and supplant manufactured goods in Arizona with less expensive products. However, this did not appear to hurt Arizona’s economy overall, since Arizona also saw a significant increase in GDP following the implementation of the USMCA."
    ),
    (
        "Trade Balance Impact", 
        "Trade_Balance_Impact_Image_2025.png", 
        "Upon the implementation of the USMCA, 18 states saw a statistically significant change in their trade balance with Mexico, mostly negative.", 
        "The USMCA’s new provisions on e-commerce likely bolstered the real estate industry, a major component of the economies of Montana and Colorado. This is because many businesses in the real estate sector, such as Airbnb and Zillow, depend on digital services. Thus, provisions such as prohibiting customs duties on electronically transmitted products and protecting cross-border data flows created a more favorable environment for these businesses, allowing the real estate industry to flourish.", 
        "Rhode Island, despite also having a dominant real estate sector, saw significant declines in both imports from and exports to Mexico, indicating less of a direct economic benefit for its real estate industry.", 
        "While most manufacturing states, including Minnesota, Wisconsin, Illinois, Ohio, Louisiana, Mississippi, and Tennessee, saw a reduction in their trade balance, Michigan and Kentucky did not. This is most likely because Michigan and Kentucky both have large vehicle manufacturing industries and benefit from the USMCA’s requirement that new motor vehicles must have at least 75% of their content sourced from North America.", 
        "However, other manufacturing states, particularly in the south, that did not have as strong an automotive sector likely suffered losses from the reduction in trade barriers, allowing cheaper goods to displace them.", 
        "While other manufacturing states, such as Ohio, also have large auto sectors, they focus more on parts manufacturing than vehicle manufacturing. Since the USMCA’s rule of origin requirement surrounding new motor vehicles targeted vehicle parts, rather than finished vehicles, states with auto industries reliant on vehicle manufacturing, such as Michigan and Kentucky, stood to benefit from these provisions at the expense of states more reliant on parts manufacturing.", 
        "Additionally, the USMCA’s focus on goods likely harmed service-based economies, including Georgia and Maryland, which rely on real estate and rental leasing, and Delaware, which relies on finance and insurance.",
        "The fact that Virginia and Massachusetts, both of which rely on professional, scientific, and technical services, saw declines in their trade balance stands as most perplexing, given the USMCA’s enhanced provisions surrounding intellectual property rights, cybercrime, and trade secret theft. Most likely, Canadian and Mexican firms benefited from these protections to a greater extent, allowing them to occupy a larger portion of the U.S. market."
    ),
    (
        "Business Startups Impact", 
        "Business_Startups_Impact_Image_2025.png", 
        "The implementation of the USMCA bolstered the quarterly business startups of eight states and only resulted in a reduction of one. Quarterly business startups reflect the number of business startups per fiscal quarter, “a three-month period in a company's financial year used for reporting earnings and paying dividends.”", 
        "The states that saw gains primarily rely on manufacturing and real estate. Indiana, Ohio, Tennessee, and Alabama primarily rely on manufacturing, and Nevada, Arizona, and Georgia primarily rely on real estate and rental leasing.",
        "Given that the USMCA had a neutral to negative effect on these states in terms of imports, exports, and trade balance, these findings suggest that these states saw an increase in quarterly business formations as a way to source more goods and services domestically or engage in trade with other countries.", 
        "Washington, with an economy primarily reliant on information, saw a reduction in quarterly business formations, supporting my earlier hypothesis that the USMCA’s enhanced provisions surrounding intellectual property rights, cybercrime, and trade secret theft benefited Mexican and Canadian firms more than U.S. firms to the detriment of the U.S. information and technology industry."
    ),
    (
        "Job Growth Impact from NAFTA", 
        "Job_Growth_Impact_Image_NAFTA.png", 
        "After the USMCA went into effect, no state saw a statistically significant change in job growth. This is likely because the new provisions of the USMCA focus more on trade flows and enhancing supply chains, which have less of a direct impact on employment.",
        "NAFTA, however, resulted in a positive, statistically significant impact on job growth for Maryland, Connecticut, Massachusetts, and New Hampshire. This is most likely because the economies of these four states primarily rely on services and finance and benefited from NAFTA’s groundbreaking provisions surrounding the liberalization of service trade."
    ),
    (
        "States with No Statistically Significant Change", 
        "No_Significant_Change_Image_2025.png", 
        "While the implementation of NAFTA and the USMCA significantly impacted 39 U.S. states on at least one metric, 11 states saw no significant change on any of the nine metrics utilized in this paper.",
        "One major reason is that populous states such as California, Texas, Florida, and New Jersey have more multifaceted economies and are less likely to be significantly impacted by implementing one trade agreement. Additionally, six of these eleven states have an economy primarily reliant on manufacturing, including Oregon, Utah, Kansas, Texas, North Carolina, and Pennsylvania. Two more, Alaska and Oklahoma, have economies primarily reliant on mining, quarrying, and oil and gas extraction.", 
        "These findings support my earlier hypothesis that the USMCA had a neutral to negative impact on the primary economic sector, which focuses on resource extraction, and the secondary economic sector, which focuses on turning raw materials into manufactured goods, of the United States."
    )
]

# Render each section
for visual in visuals:
    display_section(*visual)

# Conclusion
st.markdown("""
---

### Conclusion
""")

st.markdown("Based on the findings of this paper, the USMCA primarily had a neutral to negative effect on the economies of individual U.S. states.")

st.markdown("States primarily reliant on real estate and rental leasing, such as Idaho, Arizona, Maine, and Rhode Island, saw a neutral to positive impact from the USMCA. This indicates that the new provisions of the USMCA surrounding e-commerce, data flows, and data localization, such as prohibiting customs duties on electronically transmitted products and protecting cross-border data flows, bolstered digital services, a key component of the growth of the U.S. real estate industry.")

st.markdown("This is because many businesses in the real estate sector, such as Airbnb and Zillow, depend on digital services. Thus, the USMCA’s new provisions addressing the realm of digital trade created a more favorable environment for these businesses, allowing the real estate industry to flourish.")

st.markdown("States reliant on manufacturing, however, such as Minnesota, Wisconsin, Illinois, Louisiana, Mississippi, and Tennessee, suffered major losses.") 

st.markdown("This likely suggests that the USMCA’s new provisions, such as requiring new motor vehicles to have at least 75% of their content sourced in North America, requiring that 40-45% of auto content be made by workers earning at least $16 an hour, and “rapid response” mechanism designed to bolster workers’ rights in Mexico did not make the U.S. manufacturing industry more competitive.")

st.markdown("These provisions may have done the opposite, increasing manufacturing costs so much that it became untenable to do business. Michigan and Kentucky were the only manufacturing states to defy this trend, likely due to the presence of strong automotive sectors in their states.")

st.markdown("The USMCA’s removal of NAFTA’s energy chapter and recognition of Mexico’s complete ownership of hydrocarbons also likely damaged the U.S. mining and energy industries, given that states such as New Mexico, North Dakota, Oklahoma, and West Virginia had a neutral to negative economic impact.")

st.markdown("Additionally, the USMCA’s enhanced provisions surrounding intellectual property rights, cybercrime, and trade secret theft failed to benefit the United States economically, with states primarily reliant on information and technology, such as Washington, California, Virginia, and Massachusetts, seeing a neutral to negative economic impact.")

st.markdown("In conclusion, these findings suggest that when the USMCA is renegotiated in 2026, the leaders of the three countries involved should seek to reduce the stringent rules of origin and wage requirements that raise manufacturing costs.")

st.markdown("They should also re-evaluate and possibly strengthen the provisions surrounding intellectual property rights in a mutually beneficial way for all countries involved. Furthermore, they should reinstate NAFTA’s energy chapter, liberalize the hydrocarbon industry, and pursue other measures to strengthen the mining and energy industries of all countries.")

st.markdown("However, the leaders should also take care to preserve the USMCA’s new provisions surrounding e-commerce, data flows, and data localization, which have successfully bolstered local supply chains and the economies of U.S. states.")

st.markdown("""
---

**Author:** Isaac Santiago Nuttall  
**Source Code:** [GitHub Repository](https://github.com/IsaacNuttall/usmca-project)
""")