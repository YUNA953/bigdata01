#include <iostream>
#include <string>
using namespace std;

int main() {
	int number;
	//int count = 0;
	bool isPrime = true;  // memory size down, readability up

	cin >> number;

	if (number >= 2) {
		for (int i = 2; i < number; i++) {
			if (number % i == 0) {
				//count = count + 1;
				isPrime = false;  // remove + sign
				break;
			}
			//cout << i << " ";
		}
	}
	else {
		/*count = 1;*/
		isPrime = false;
	}

	//if (count == 0) {
	if (isPrime) {  // remove == sign
		cout << number << "는(은) 소수입니다.\n";
	}
	else {
		cout << number << "는(은) 소수가 아닙니다!\n";
	}

	return 0;
}

//#include <iostream>
//#include <string>
//using namespace std;
//
//int main() {
//	int number;
//	int count = 0;
//
//	cin >> number;
//
//	if (number >= 2) {  // bug fix
//		for (int i = 2; i < number; i++) {
//			if (number % i == 0) {
//				count = count + 1;
//				break;  // performance up
//			}
//			//cout << i << " ";
//		}
//	}
//	else {
//		count = 1;
//	}
//
//
//	if (count == 0) {
//		cout << number << "는(은) 소수입니다.\n";
//	}
//	else {
//		cout << number << "는(은) 소수가 아닙니다!\n";
//	}
//
//	return 0;
//}


//#include <iostream>
//#include <string>
//using namespace std;
//
//int main() {
//	int number;
//	int count = 0;
//
//	cin >> number;
//
//	for (int i = 1; i <= number; i++) {
//		if (number % i == 0) {
//			count = count + 1;
//		}
//		cout << i << " ";
//	}
//
//	if (count == 2) {
//		cout << number << "는(은) 소수입니다.\n";
//	}
//	else {
//		cout << number << "는(은) 소수가 아닙니다!\n";
//	}
//
//	return 0;
//}