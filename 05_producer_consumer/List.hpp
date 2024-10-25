#ifndef LIST_HPP
#define LIST_HPP

#include <exception>
#include <string>

/* CLASS DEFINITION */

template <class T>
class List {
private:
    class Node;

    public:
        typedef Node* Position;
        class Exception : public std::exception {
        private:
        std::string msg;

        public:
            Exception() noexcept : msg("Error Indefinido") {}
            Exception(const Exception& ex) noexcept : msg(ex.msg) {}
            Exception(const std::string& m) : msg(m) {}
            Exception& operator=(const Exception& ex) noexcept {
                msg = ex.msg;
                return *this;
            }
            virtual ~Exception() {}
            virtual const char* what() const noexcept { return msg.c_str(); }
        };

    private:
        class Node {
        private:
            T* dataPtr;
            Position next;
            Position prev;

        public:
            class Exception
                : public List::Exception {  // Se usa herencia apra evitar redundancia
                using List::Exception::Exception;  /// Para evitar problemas con los
                                                    /// constructores
                };

            Node();
            Node(const T&);
            ~Node();

            T* getDataPtr();  // Puede causar conflicto agregar un const
            T getData() const;
            Position getNext() const;
            Position getPrev() const;

            void setDataPtr(T*);
            void setData(const T&);
            void setNext( Position&);
            void setPrev( Position&);
        };

    Position* header;
    bool isValidPos(const Position&) const;
    void copyAll(const List&);

public:
    List();
    List(const List&);
    ~List();

    bool isEmpty() const;
    void insertData(const Position&, const T&);
    void deleteData(const Position&);

    Position getFirstPos() const;
    Position getLastPos() const;
    Position getPrevPos(const Position&) const;
    Position getNextPos(const Position&) const;

    Position findData(const T&) const;

    T retrieve(const Position&) const;

    void deleteAll();

    std::string toString() const;

    List& operator=(const List&);
};

# endif

/* CLASS IMPLEMENTATION */