# Police Citizen Manager Version 2
Police Citizen Manager is a Graphical User Interface project, made with Python. This project was constructed for my local Police Department, in order to provide a better and more convinient way of managing the citizens visiting the department on a daily routine.

## Download Repository
To download the repository, you can either clone its url using the following command:
```
git clone https:/github.com/AntonisZks/Police-Citizen-Manager-App.git
```
or download the [zip file](https://github.com/AntonisZks/Police-Citizen-Manager-App/archive/refs/heads/main.zip) containing all the code and assets. 

## Running the code
To run the application you need to have [Python 3.9 and above](https://www.python.org/downloads/) installed on your system. After you have downloaded the code on your computer, the next thing you need to do is to install some **requirements files** so as the program can run correctly. You can open up a terminal window, locate the folder containing the project and execute the following command: 
```
pip install -r requirements.txt
``` 
After installing the appropriate files, you can execute the program, either by opening your favourite Python IDE and run the `main.py` file or by opening a terminal window and executing the following command: 
```
python main.py
```
> [!IMPORTANT]
> For both cases make sure you are on the correct folder that contains the `main.py` file. If everything went right, the application should start running.

## Starting the Application
By starting the application, the users are introduced with a window containing an empty panel. This panel is responsible to keep a variety of `Excel files`. Below there is an `Add Button` that allows the users to select an Excel file from their system to work with. This Excel file will then be stored inside that panel and it will be set as **stored file** in the application. The users can of course remove every stored file from the panel at any time. After an Excel file has been set as stored, the users can **click** on it in order to manage the records inside it. The application will then introduce a `starting menu` for the user, which contains the basic methods for managing the records inside the Excel file.
> [!NOTE]
> Whenever the users restart the application, the stored files in the panel won't be lost.

## Methods
The application provides 4 basic methods for managing the records' data.
- Search
- Insert
- Edit
- Delete

## Search Method
### Searching for records
The first method is **searching**. The application allows the users to search for **specific records**, inside the Excel file they have chosen to manage. They can search for records according to their:
- Folder ID
- Surname

> [!NOTE]
> - The `folder ID` is often **unique** for every record, so the users have to type the full folder ID.
> - Meanwhile the `surname` option has a different approach. The users can search for a specific surname, by typing a part that starts with it, and the program will return all the records that their surname starts with the given users' entrance.

### Search Results
After the user search for specific records, the program returns a **list of records** that agree on the searching conditions by the user. The list is made by `buttons` that each one has a **label** containing the record's name, surname and fathername. The list is shown **below the searching input fields**, and the users can click on several buttons. The selected buttons will reveal their **content** on the **right side of the screen**. The contents of every buttons are the corresponding `record's data`.

## Insert Method
The users can **insert** new records inside the Excel file they are editing. By clicking on the `Insert button` a **new form** is appeared waiting to be filled. The first field of the form is the `folder ID`. By default the program calculates the **next available folder ID** and fills the field with it, but the users can of course change it if needed. The other fields correspond to each `records data`. The users can leave most of them empty, excluding the **Folder ID** and the **Surname**, that they are **essential** for the application. 
> [!NOTE]
> The program also forces the users to enter a correct **birthdate** and a **phone number**, by having a specific `prototype` for each one:
> - The birthdate has to follow the following prototype `DD/MM/YYYY`.
> - The phone number must contain `10 digits`.

## Edit & Delete Methods
The third option of the application is `Editing`. This option although contains both the `Edit` and `Delete` methods of the application. Specifically:
- The **Edit** method allows the users to change the **data of specific records** inside the Excel file and **save** those changes. It follows the **same graphical design** such as the **Search Method**. The only **difference** is that the users can actually `edit` this time the **fields returned** by the **searching process**.
- The **Delete method** can bw used to **delete** specific records from the Excel file. The users fist **searches** for the records they want to delete and after **selecting** the ones they wish, they **click** on the `Delete button`.
> [!NOTE]
> - In order to keep privacy of the Excel files' contents, the `Editing` method requires a `password` to let the users have access to records' **editing** and **deleting** methods.
> - The users have to define their **password**, when they start the application for the first time.
> - The users can also change their password of course at any time.
