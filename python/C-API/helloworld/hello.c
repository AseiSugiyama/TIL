#include <stdio.h>
#include <Python.h>

// Since long type is gone in Python 3, 
// PyInt_FromLong is not exist in Python 3 C-API
#if PY_MAJOR_VERSION >= 3
#define PyInt_FromLong PyLong_FromLong
#endif

// Module method definitions
static PyObject* hello_world(PyObject *self, PyObject *args) {
    printf("Hello, world!\n");
    Py_RETURN_NONE;
}

static PyObject* hello(PyObject *self, PyObject *args) {
    const char* name;
    if (!PyArg_ParseTuple(args, "s", &name)) {
        return NULL;
    }

    printf("Hello, %s!\n", name);
    Py_RETURN_NONE;
}

static PyObject* print_int_value(PyObject *self, PyObject *args){
    long number;
    if (!PyArg_ParseTuple(args, "l", &number))
    {
        return NULL;
    }

    printf("value is %ld!\n", number);
    Py_RETURN_NONE;
}

static PyObject* hundle_bytes_as_string(PyObject *self, PyObject *args){
    PyObject *buff;
    if (!PyArg_ParseTuple(args, "S", &buff))
    {
        return NULL;
    }

    printf("value is %s!\n", PyBytes_AsString(buff));
    Py_RETURN_NONE;
}

// Method definition object for this extension, these argumens mean:
// ml_name: The name of the method
// ml_meth: Function pointer to the method implementation
// ml_flags: Flags indicating special features of this method, such as
//          accepting arguments, accepting keyword arguments, being a
//          class method, or being a static method of a class.
// ml_doc:  Contents of this method's docstring
static PyMethodDef hello_methods[] = {
    {"hello_world", hello_world, METH_NOARGS,
     "Print 'hello world' from a method defined in a C extension."},
    {"hello", hello, METH_VARARGS,
     "Print 'hello xxx' from a method defined in a C extension."},
    {"print_int_value", print_int_value, METH_VARARGS,
     "Print 'value is xxx' from a method defined in a C extension."},
    {"hundle_bytes_as_string", hundle_bytes_as_string, METH_VARARGS,
     "Print 'value is xxx' from a method defined in a C extension."},
    {NULL, NULL, 0, NULL}};

#if PY_MAJOR_VERSION >= 3
// #define PyInteger_FromLong(x) PyLong_FromLong(x)
// #else
// #define PyInteger_FromLong(x) PyInt_FromLong(x)

// Module definition
// The arguments of this structure tell Python what to call your extension,
// what it's methods are and where to look for it's method definitions
static struct PyModuleDef hello_definition = { 
    PyModuleDef_HEAD_INIT,
    "hello",
    "A Python module that prints 'hello world' from C code.",
    -1, 
    hello_methods
};

// Module initialization
// Python calls this function when importing your extension. It is important
// that this function is named PyInit_[[your_module_name]] exactly, and matches
// the name keyword argument in setup.py's setup() call.
PyMODINIT_FUNC PyInit_hello(void) {
    Py_Initialize();
    return PyModule_Create(&hello_definition);
}
#else
PyMODINIT_FUNC inithello(void)
{
    Py_InitModule3("hello",
                   hello_methods, "A Python module that prints 'hello world' from C code.");
}
#endif
