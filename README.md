### **Description**

It is a simple and low Python knowledge project that describes the instant weather code structure and sample structure that gives files in html format. It has a messy structure because it is the first ‘useful’ project I made with Python, but it works. All of the examples are in Turkish because I live in Turkey. When you do not translate the code, you will see results in English, which is the default language.

I've also used some translation programmes to make it easier for more people to understand, so it's likely to be difficult to understand. I would like to solve problems by asking questions.

### **Required Libraries and API** 

- requests
- folium
- from folium import Icon, Popup
- datetime

The API called Weather API is used as the API. OpenWeather allows 1000 calls per day for this API for free. https://openweathermap.org/api

### **Features**

- You can see instant data of any city in the world. Since these data are collected with the device closest to the coordinate you specify, you get the best data. (At least this is claimed to be the case for the most data collection and when I made comparisons, it always gave correct results).
- As many coordinates as desired can be added. Since this feature is supported both in the API and in the code, there is no incompatibility BUT increasing the number of coordinates delays the generation of the .html file.
- It works with a code consisting of a simple and single file. Normally the content is in different files, but it is a single file because it is not a complex system.
- It is possible to improve. Although it is accurate and has extra features, it is suitable for automation system. It is also simple to develop visually. 
- Free of charge. The API meets 1000 calls per day free of charge and never reaches 1000 usage due to its purpose.
- It has OpenWeather support. That is, it is the same as the structure of many weather applications we already use. Also, not all API features are even used in this project. In other words, the existing code is open to development by OpenWeather.

### **What does it look like?**

![Screenshot_1](https://github.com/user-attachments/assets/7d41342d-d53f-4757-8027-3c2825ef2363)
![Screenshot_2](https://github.com/user-attachments/assets/c8056703-540e-41b4-a248-43b7e5fa9c2b)
![Screenshot_3](https://github.com/user-attachments/assets/e5eba61c-0552-4fa6-8c14-cb37d3160cbd)

### **All versions**

0.9 Last Test https://github.com/Zephyrquill/htmlweather/releases/tag/Beta

### **Warnings**

- Using the OpenWeather API brings some responsibilities. You need to pay attention to these. You need to pay attention to the possibility of errors or omissions in the code. There is a disclaimer.
- When the code runs, you may have to wait longer than you expected. In this case, there may be a problem with the OpenWeather system, but the API data collection may have taken a long time due to the large number of coordinates. In this case, NEVER run the code again and again. Just wait. You can ask questions if you think there is a problem.
- Your code has nothing to do with working and I have nothing to do with OpenWeather. We only use their services.
- There is no information on the use and evolution of the system and its monetisation. Firstly, this is not the purpose of the code. Moreover, you need to investigate this issue according to the type of API used.
