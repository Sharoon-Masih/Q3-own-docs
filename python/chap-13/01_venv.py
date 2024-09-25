# A virtual environment in Python is a self-contained, isolated environment that allows you to manage and use different versions of Python packages and dependencies for different projects. It helps prevent conflicts between packages and ensures that your projects remain stable and reproducible, regardless of changes or updates to global Python packages.

# ab let suppose we are working with pandas library, ab muja project may pandas may 1.5.0 version use krna hai or uska 2.2.2 version be use krna hai. toh ab dono version toh at the same time ek hi project ma nhi chl sktay toh iss lia hum jo version globally use krna hai usko direct project ma install krleinga or jo virtual ma krna hai uskay liya virtual environment create kreinga.

# To create a virtual environment, 
# 1. Open your terminal or command prompt.
# 2. Navigate to the project where you want to create the virtual environment.
# 3. 'pip install virtualenv' package.'folderName' usme virtual environment create hojayega, then phr uss virtual environment may further jo be install krna hai we can do it easily and jo be install kreingay uska taluk srf uss virtual environment say hota hai uskay bahir uska koi taluk nhi bcuz it is isolated environment.
# 4. 'virtualenv folderName' by doing this we can create virtual env or jo agay folderName likhaga wo new folder create hojayega or usme virtual env create hojayegi. or yeh project ma 'virtual_env' folder create hua hai yeh wohi folder hai jo humna 'virtualenv' package ka through kia hai install. 
  
# 5. remember virtual environment ma koi be kam krnay say pehlay usko activate krna hai, or then phr agr again global environment pa move krna hai toh virtual environment ko deactivate krna hai.
 
# 6. remember jo vscode may powershell hai usme folderName nhi likha ayega jab virtual environment activate hojaye toh iss lia virtual environment ko activate krnay kay liya cmd pa chechk krsktay hain. 
# 7. to activate write this command on cmd : .\folderName\Scripts\activate
# 8. to deactivate write this command on cmd : deactivate