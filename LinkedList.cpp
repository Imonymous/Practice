#include<iostream>

using std::cout;
using std::endl;

class Node {
	public:
		int data;
		Node *next;
		Node(int d) {
			data = d;
		}

		void appendToTail(int d) {
			Node *end = new Node(d);
			Node *n = this;
			while (n->next != NULL) {
				n = n->next;
			}
			n->next = end;
			end->next = NULL;
		}
};

removeDuplicates(Node *head) {

	Node *n = head;
	std::vector<int> v;

	while (n->next != null) {
		if ( )
	}


}

int main() {

	Node *primes = new Node(2);

	primes->appendToTail(3);
	primes->appendToTail(5);
	primes->appendToTail(7);
	primes->appendToTail(5);
	primes->appendToTail(7);
	primes->appendToTail(11);
	primes->appendToTail(13);
	primes->appendToTail(17);

	Node *n = primes;

	while (n->next != NULL) {
		cout<<n->data<<endl;
		n = n->next;
	}

	// removeDuplicates(primes);

}