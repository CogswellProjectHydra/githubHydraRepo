#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <process.h>

using namespace std;

template<typename dataType>
class repl {
public:
	repl (dataType target, dataType replacement) {
		_target = target;
		_replacement = replacement;
	}
	inline dataType operator() (dataType ch)  {
		if (ch == _target) return _replacement;
		return ch;
	};
private:
	char _target, _replacement;
};


char *copyString (string s) {
	const int size = 1 + s.length ();
	char *ret = new char[size];
	strcpy_s (ret, size, s.c_str ());
	return ret;
}

int main (int argc, char * argv[]) {
	
	cout << endl;

	if (argc != 2) {
		cerr << "Expected exactly 1 argument, a Maya scene file." << endl;
		exit (-1);
	}

	string mayaFile (argv[1]);
	transform (mayaFile.begin (), mayaFile.end (), 
			   mayaFile.begin (), repl<char> ('\\', '/'));

	if (mayaFile.substr (mayaFile.length () - 3) != ".ma" &&
		mayaFile.substr (mayaFile.length () - 3) != ".mb") {
			cerr << mayaFile << " is neither a .ma nor a .mb file." << endl;
			exit (-1);
	}

	int scenePos = mayaFile.find ("/scenes/");
	if (scenePos == mayaFile.npos) {
		cerr << mayaFile << " isn't in a /scenes/ folder." << endl;
		exit (-1);
	}

	string project = mayaFile.substr (0, scenePos);
	cout << "Project folder is " << project << endl;

	cout << "Enter start frame: ";
	string startFrame;
	cin >> startFrame;

	cout << "Enter end frame: ";
	string endFrame;
	cin >> endFrame;

	stringstream cmd;
	char maya[] = "\"c:\\program files\\autodesk\\maya2011\\bin\\render.exe\"";

	cmd << maya
		<< " -proj " << project
		<< " -s " << startFrame 
		<< " -e " << endFrame
		<< " " << mayaFile;

	const char * cmds = copyString (cmd.str ());
	cout << "Command string: " ;
	cout << cmds << endl;
	system (cmds);
}