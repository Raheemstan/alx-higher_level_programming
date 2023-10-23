#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    if (PyBytes_Check(p)) {
        printf("  size: %zd\n", PyBytes_Size(p));
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first %zd bytes: ", PyBytes_Size(p) + 1);
        for (Py_ssize_t i = 0; i <= PyBytes_Size(p) && i < 10; i++) {
            printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
            if (i < PyBytes_Size(p))
                printf(" ");
        }
        printf("\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_list(PyObject *p) {
    printf("[*] Python list info\n");
    if (PyList_Check(p)) {
        printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
        printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
        for (Py_ssize_t i = 0; i < PyList_Size(p); i++) {
            printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
            if (PyBytes_Check(PyList_GetItem(p, i))) {
                print_python_bytes(PyList_GetItem(p, i));
            }
        }
    } else {
        printf("  [ERROR] Invalid List Object\n");
    }
}

void print_python_float(PyObject *p) {
    printf("[.] float object info\n");
    if (PyFloat_Check(p)) {
        printf("  value: %lf\n", PyFloat_AsDouble(p));
    } else {
        printf("  [ERROR] Invalid Float Object\n");
    }
}
