//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop
#include <System.Diagnostics.hpp>

#include "Unit3.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm3 *Form3;

using namespace std;
//---------------------------------------------------------------------------
__fastcall TForm3::TForm3(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TForm3::Button1Click(TObject *Sender)
{
  if (Edit1->Text.IsEmpty()) {
        MessageBoxA(NULL, "Por favor, insira um texto no campo.", "Aviso", MB_OK | MB_ICONWARNING);
        return;
    }

    UnicodeString pythonScript = "gqrcode.py";
    UnicodeString qrCodeFile = "qrcode.png";
    UnicodeString link = Edit1->Text;

    UnicodeString command = "python \"" + pythonScript + "\" \"" + link + "\" \"" + qrCodeFile + "\"";
    AnsiString commandAnsi = command;

    int result = WinExec(commandAnsi.c_str(), SW_HIDE);

    Sleep(500);

    if (result > 31) {
        TImage *image = new TImage(this);
        try {
            image->Picture->LoadFromFile(qrCodeFile);
            Image1->Picture->Assign(image->Picture);
        } __finally {
            delete image;
        }
    } else {
        MessageBoxA(NULL, "Erro ao gerar QR Code. Verifique se o script Python está correto.", "Erro", MB_OK | MB_ICONERROR);
    }
}
//---------------------------------------------------------------------------
void __fastcall TForm3::FormCreate(TObject *Sender)
{
WinExec("pip install -r requirements.txt", SW_HIDE);
}
//---------------------------------------------------------------------------
void __fastcall TForm3::FormClose(TObject *Sender, TCloseAction &Action)
{
UnicodeString qrCodeFile = "qrcode.png";
    if (FileExists(qrCodeFile)) {
        DeleteFile(qrCodeFile);
    }
}
//---------------------------------------------------------------------------
