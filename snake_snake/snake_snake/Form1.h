#pragma once
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

namespace snake_snake {

	using namespace std;
	using namespace System;
	using namespace System::IO; 
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;
	using namespace System::Threading;
	int t;
				

	/// <summary>
	/// Сводка для Form1
	/// </summary>
	public ref class Form1 : public System::Windows::Forms::Form
	{
	public:
		Form1(void)
		{
			InitializeComponent();

			
			
			//
			//TODO: добавьте код конструктора
			//
		}

	protected:
		/// <summary>
		/// Освободить все используемые ресурсы.
		/// </summary>
		~Form1()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::TextBox^  textBox1;
	private: System::Windows::Forms::TextBox^  textBox2;
	private: System::Windows::Forms::Button^  button1;
	private: System::Windows::Forms::PictureBox^  pictureBox1;
	private: System::Windows::Forms::Button^  button2;
	private: System::Windows::Forms::Label^  label1;
	private: System::Windows::Forms::Button^  button3;
	private: System::Windows::Forms::Button^  button4;



	protected: 

	private:
		/// <summary>
		/// Требуется переменная конструктора.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Обязательный метод для поддержки конструктора - не изменяйте
		/// содержимое данного метода при помощи редактора кода.
		/// </summary>
		void InitializeComponent(void)
		{
			this->textBox1 = (gcnew System::Windows::Forms::TextBox());
			this->textBox2 = (gcnew System::Windows::Forms::TextBox());
			this->button1 = (gcnew System::Windows::Forms::Button());
			this->pictureBox1 = (gcnew System::Windows::Forms::PictureBox());
			this->button2 = (gcnew System::Windows::Forms::Button());
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->button3 = (gcnew System::Windows::Forms::Button());
			this->button4 = (gcnew System::Windows::Forms::Button());
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^  >(this->pictureBox1))->BeginInit();
			this->SuspendLayout();
			// 
			// textBox1
			// 
			this->textBox1->Location = System::Drawing::Point(509, 43);
			this->textBox1->Name = L"textBox1";
			this->textBox1->Size = System::Drawing::Size(134, 20);
			this->textBox1->TabIndex = 0;
			this->textBox1->TextChanged += gcnew System::EventHandler(this, &Form1::textBox1_TextChanged);
			// 
			// textBox2
			// 
			this->textBox2->Location = System::Drawing::Point(509, 102);
			this->textBox2->Name = L"textBox2";
			this->textBox2->Size = System::Drawing::Size(134, 20);
			this->textBox2->TabIndex = 1;
			this->textBox2->TextChanged += gcnew System::EventHandler(this, &Form1::textBox2_TextChanged);
			// 
			// button1
			// 
			this->button1->Location = System::Drawing::Point(509, 248);
			this->button1->Name = L"button1";
			this->button1->Size = System::Drawing::Size(134, 49);
			this->button1->TabIndex = 2;
			this->button1->Text = L"button1";
			this->button1->UseVisualStyleBackColor = true;
			this->button1->Click += gcnew System::EventHandler(this, &Form1::button1_Click);
			// 
			// pictureBox1
			// 
			this->pictureBox1->Location = System::Drawing::Point(68, 43);
			this->pictureBox1->Name = L"pictureBox1";
			this->pictureBox1->Size = System::Drawing::Size(400, 300);
			this->pictureBox1->TabIndex = 3;
			this->pictureBox1->TabStop = false;
			this->pictureBox1->Click += gcnew System::EventHandler(this, &Form1::pictureBox1_Click);
			// 
			// button2
			// 
			this->button2->Location = System::Drawing::Point(509, 303);
			this->button2->Name = L"button2";
			this->button2->Size = System::Drawing::Size(133, 48);
			this->button2->TabIndex = 4;
			this->button2->Text = L"button2";
			this->button2->UseVisualStyleBackColor = true;
			this->button2->Click += gcnew System::EventHandler(this, &Form1::button2_Click);
			// 
			// label1
			// 
			this->label1->AutoSize = true;
			this->label1->Location = System::Drawing::Point(27, 43);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(35, 13);
			this->label1->TabIndex = 5;
			this->label1->Text = L"label1";
			// 
			// button3
			// 
			this->button3->Location = System::Drawing::Point(508, 195);
			this->button3->Name = L"button3";
			this->button3->Size = System::Drawing::Size(134, 47);
			this->button3->TabIndex = 6;
			this->button3->Text = L"button3";
			this->button3->UseVisualStyleBackColor = true;
			this->button3->Click += gcnew System::EventHandler(this, &Form1::button3_Click);
			// 
			// button4
			// 
			this->button4->Location = System::Drawing::Point(509, 142);
			this->button4->Name = L"button4";
			this->button4->Size = System::Drawing::Size(134, 47);
			this->button4->TabIndex = 7;
			this->button4->Text = L"button4";
			this->button4->UseVisualStyleBackColor = true;
			this->button4->Click += gcnew System::EventHandler(this, &Form1::button4_Click);
			// 
			// Form1
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 13);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->ClientSize = System::Drawing::Size(682, 383);
			this->Controls->Add(this->button4);
			this->Controls->Add(this->button3);
			this->Controls->Add(this->label1);
			this->Controls->Add(this->button2);
			this->Controls->Add(this->pictureBox1);
			this->Controls->Add(this->button1);
			this->Controls->Add(this->textBox2);
			this->Controls->Add(this->textBox1);
			this->Name = L"Form1";
			this->Text = L"Змейка";
			this->Load += gcnew System::EventHandler(this, &Form1::Form1_Load);
			(cli::safe_cast<System::ComponentModel::ISupportInitialize^  >(this->pictureBox1))->EndInit();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void textBox1_TextChanged(System::Object^  sender, System::EventArgs^  e) {
			 }
	private: System::Void Form1_Load(System::Object^  sender, System::EventArgs^  e) {  //инициализация элементов формы
		    this->label1->Visible = false;
			this->textBox1->Text = "Введите уровень 1-10";	 
			this->textBox2->Text = "Введите свой ник";
			this->button1->Text = "Начать игру";
			this->button2->Text = "Показать справку";
			this->button3->Text = "Инициализация игрового поля";
			this->button4->Text = "Результаты предыдущих игр";
			 }
	private: System::Void button1_Click(System::Object^  sender, System::EventArgs^  e) {      //кнопка к началу игры

				 int p=4; //инициализация признака характеризующего направление движения
				 int s=1; //инициализация выключателя цикла
				 int g;
				 int i=0,j=0; //счетчик для длины змейки
				 int xmas[5],ymas[5];
				 t=System::Int32::Parse(textBox1->Text);
				 int x0,x1,y0,y1; //текущие координаты для отрисовки
				 x0=200;  //начальные координаты х
				 y0=200;  //начальные координаты у
				 Graphics ^graf1;
				 Pen^ Pen1 = gcnew Pen( Color::Green,15.0f ); //задаю параметры линии для отрисовки змейки
				 Pen^ Pen0 = gcnew Pen( Color::White,15.0f ); //задаю параметры линии для отрисовки змейки
			     graf1 = pictureBox1->CreateGraphics();   //инициализирую поле для рисования на pictureBox1 

				 while(s){
					      g = getch();
						  i = static_cast<int>(g);
						  if (g==1){p=1;};
						  if (g==2){p=2;};
						  if (g==3){p=3;};
						  if (g==4){p=4;};

					 if(j>4){
				            xmas[1] = xmas[2];                   //ползет змейка
							 ymas[1] = ymas[2];
							 xmas[2] = xmas[3];  //ползет змейка
							 ymas[2] = ymas[3];
							 xmas[3] = xmas[4];  //ползет змейка
							 ymas[3] = ymas[4];
							 xmas[4] = x1;
							 ymas[4] = y1;       //накопилась длина змейки
							 graf1->DrawLine(Pen0, xmas[0], ymas[0], xmas[1], ymas[1]);
					 }else{xmas[j]=x0;ymas[j]=y0;};
					 ;
					 if (p==1) //признак движения вверх
					 {
						x1=x0;
						y1 = y0+15;
					 };
					 if (p==2) //признак движения вниз
					 {
						x1=x0;
						y1 = y0-15;
					 };
					 if (p==3) //признак движения влево
					 {
						x1=x0-15;
						y1 = y0;
					 };
					 if (p==4) //признак движения вправо
					 {
						x1=x0+15;
						y1 = y0;
					 };
					 if (x1>400) //столкновение с границей
					 {
						s = 0;
					 };
					 if (x1<0)
					 {
						s = 0;
					 }; 
                     if (y1<0)
					 {
						 s = 0; 	}
					 if (y1>300)
					 {
						s = 0;
					 };

					 graf1->DrawLine(Pen1, x0, y0, x1, y1);
					 x0=x1;
					 y0=y1;
					 j = j+1;
					 Thread::Sleep(t*100);
				 };
				 String^ fileName = "textfile.txt";  
				 StreamWriter^ sw = gcnew StreamWriter(fileName);
				 sw->Write(this->textBox2->Text); 
				 sw->Write("| Количество очков (время жизни змейки)");
				 sw->Write(j); 
				 sw->Close(); 
				 
							 //тут надо добавить запись в файлck(System::Object^  sender, System::EventArgs^  e) {
				 
			 };
private: System::Void button2_Click(System::Object^  sender, System::EventArgs^  e) {     //кнопка к показу справки
			 this->pictureBox1->Visible = false;
			 this->label1->Visible = true;
			 this->label1->Text = "Программа Змейка, написана на Visual C++, отрисовка реализована посредством \n pictureBox, к программе приложен текстовой файл хранящий результаты последних игр.";

		 }
private: System::Void button3_Click(System::Object^  sender, System::EventArgs^  e) {

				 this->pictureBox1->Visible = false;
				 this->label1->Visible = false;
				 this->pictureBox1->Visible = true;
				 this->pictureBox1->BackColor = Color::White;

		 }
private: System::Void pictureBox1_Click(System::Object^  sender, System::EventArgs^  e) {
		 }
private: System::Void textBox2_TextChanged(System::Object^  sender, System::EventArgs^  e) {
		 }
private: System::Void button4_Click(System::Object^  sender, System::EventArgs^  e) {
			 			 this->pictureBox1->Visible = false;
			 this->label1->Visible = true;
			 StreamReader^ stream = File::OpenText("textfile.txt");
    if (String^ s = stream->ReadLine())
        this->label1->Text = s;
    delete (IDisposable^)stream;

		 }
};

}