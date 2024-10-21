#ifndef NODE_HPP
#define NODE_HPP

#include <iostream>

/* CLASS DEFINITION */

template <class T>
class Node {
    private:
        T data;
        Node* next;
        Node* prev;

    public:
        Node();
        Node(const T&);

        T getData() const;
        Node* getNext();
        Node* getPrev();

        void setData(const T&);
        void setNext(Node*);
        void setPrev(Node*);
};

#endif

/* CLASS IMPLEMENTATION */

using namespace std;

template<class T>
Node<T>::Node() : prev(nullptr), next(nullptr) {

}

template<class T>
Node<T>::Node(const T& e) : data(e), prev(nullptr) next(nullptr) {

}

template<class T>
T Node<T>::getData() const {
	return data;
}

template<class T>
Node<T>* Node<T>::getNext() {
	return next;
}

template<class T>
Node<T>* Node<T>::getPrev() {
	return prev;
}

template<class T>
void Node<T>::setData(const T& e) {
	data = e;
}

template<class T>
void Node<T>::setNext(Node* p) {
	next = p;
}

template<class T>
void Node<T>::setPrev(Node* p) {
	next p;
}