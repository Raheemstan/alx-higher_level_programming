#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %zd\n  trying string: %s\n  first 10 bytes: ", size, str);

    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x", str[i] & 0xFF);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n  value: %f\n", PyFloat_AS_DOUBLE(p));
}
