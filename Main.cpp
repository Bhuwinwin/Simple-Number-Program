#include <iostream>
using namespace std;

void Program1();
void Program2();
void Program3();

int main() {
    //cout << "TEST!" << endl;
    //Works
    //Func!
    
    int index;
    
    cout << "----- NUMBER PROGRAM -----\n";
    cout << ". \n";
    cout << " * INDEX * " << endl;
    cout << "[1] = Find Price per People!\n";
    cout << "[2] = Make a Arrange of Whole Student EXAM Score!\n";
    cout << "[3] = 2 ditits Calculator!\n";
    cout << ". \n";
    cout << "Plese ENTER to Number of INDEX here! => ";
    cin >> index;
    cout << ".\n";

    
    switch (index) {
    case 1:
        Program1();
        break;
    case 2:
        Program2();
        break;
    case 3:
        Program3();
        break;
    default:
        cout << " * ERROR * " << endl;
        cout << "- Plese ENTER Correct NUMBERS! \n";
        break;
    }

}

    
void Program1() {
    int price;
    int people;
    int total;
    
    cout << "----- ProgramA : Find Price Per Perple! -----" << endl;
    cout << ".\n";
    cout << "Plese Enter the Price! => ";
    cin >> price;
    cout << "Plese Enter amout of people! => ";
    cin >> people;
    cout << ".\n";
    
    cout << "----- Price per People is!! -----\n";
    for (int count = 1; count <= people; count++) {
        total = price * count;
        cout << price << " x " << count << " = " << total << " ! " << endl;
    }

}


void Program2() {
    int student;
    int score;
    int total;
    int avg;

    cout << "----- ProgramB : Make a Arrange of Whole Student EXAM Score! -----\n";
    cout << ".\n";
    cout << "Plese Enter Your Amout of Students => ";
    cin >> student;
    cout << ".\n";
    
    for (int count = 1; count <= student; count++) {
        cout << "Plese ENTER Score of " << count << "person! =>";
        cin >> score;
        
        total += score;
        avg = total / student;
    }

    cout << "AVG Score is => " << avg << endl;
    cout << "." << endl;
    

}

void Program3() {
    void Plus();
    void Minus();
    void Mutiply();
    void Devide();
    
    int i;
    cout << "----- ProgramC : 2 ditits Calculator! -----\n";
    cout << ".\n";
    cout << "* INDEX *" << endl;
    cout << "[1] = Plus\n";
    cout << "[2] = Minus\n";
    cout << "[3] = Mutiply\n";
    cout << "[4] = Devided\n";
    cout << ".\n";
    cout << "Plese Enter Your Operation! => ";
    cin >> i;

    switch (i) {
    case 1:
        Plus();
        break;
    case 2:
        Minus();
        break;
    case 3:
        Mutiply();
        break;
    case 4:
        Devide();
        break;
    default:
        break;
    }
}

void Plus() {
        int num1;
        int num2;
        
        cout << "===== PLUS =====\n";
        cout << "Plese Enter The First NUMBERS => ";
        cin >> num1;
        cout << "Plese Enter The Secound NUMBERS => ";
        cin >> num2;
        int sum = num1 + num2;
        cout << "Answer is => " << sum;
}

void Minus() {
    int num1;
    int num2;
        
    cout << "===== MINUS =====\n";
    cout << "Plese Enter The First NUMBERS => ";
    cin >> num1;
    cout << "Plese Enter The Secound NUMBERS => ";
    cin >> num2;
    int sum = num1 - num2;
    cout << "Answer is => " << sum;
}

void Mutiply() {
    int num1;
    int num2;
        
    cout << "===== MUTIPLY =====\n";
    cout << "Plese Enter The First NUMBERS => ";
    cin >> num1;
    cout << "Plese Enter The Secound NUMBERS => ";
    cin >> num2;
    int sum = num1 * num2;
    cout << "Answer is => " << sum;
}

void Devide() {
    int num1;
    int num2;
        
    cout << "===== DEVIDED =====\n";
    cout << "Plese Enter The First NUMBERS => ";
    cin >> num1;
    cout << "Plese Enter The Secound NUMBERS => ";
    cin >> num2;
    int sum = num1 / num2;
    cout << "Answer is => " << sum;
}