#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *element = ((PyListObject *)p)->ob_item[i];
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_GET_SIZE(p);
    char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %zd\n  trying string: %s\n  first 10 bytes: ", size, str);

    for (Py_ssize_t i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", str[i] & 0xFF);
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

    double value = ((PyFloatObject *)p)->ob_fval;
    printf("[.] float object info\n  value: %f\n", value);
}
