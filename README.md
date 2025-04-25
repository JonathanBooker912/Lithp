# Lithp

A Lisp-inspired programming language with a unique phonetic twist. Lithp uses prefix notation and follows a simple syntax where expressions are enclosed in parentheses.

## Installation

```bash
git clone <repository-url>
python lithp.py <filename>
```

## Language Reference

| Construct   | Description            | Syntax Example                       |
| ----------- | ---------------------- | ------------------------------------ |
| `( )`       | Expression grouping    | `(pluth 1 2)`                        |
| `thet`      | Variable assignment    | `thet x 42`                          |
| `dithplay`  | Print to stdout        | `dithplay "Hello"`                   |
| `athk`      | Read from stdin        | `athk prompt_var target_var`         |
| `pluth`     | Addition/string concat | `(pluth 1 2)` or `(pluth "a" "b")`   |
| `timeth`    | Multiplication         | `(timeth 3 4)`                       |
| `indexth`   | String indexing        | `(indexth "hello" 1)`                |
| `repeathh`  | Numeric loop           | `repeathh i 5 { dithplay i }`        |
| `iterateth` | String iteration       | `iterateth c "hello" { dithplay c }` |

## Examples

### Basic Arithmetic and String Operations

```lithp
thet a 10
thet b 20
dithplay (pluth a b)
dithplay (timeth a b)
dithplay (pluth "Hello " "World")
```

### String Manipulation

```lithp
thet str "Lithp"
dithplay (indexth str 0)
iterateth c str {
    dithplay c
}
```

### Interactive Program

```lithp
thet name ""
thet name_prompt "Enter your name: "
athk name_prompt name
dithplay (pluth "Hello, " name)

thet count 0
thet count_prompt "Enter a number: "
athk count_prompt count
repeathh i count {
    dithplay (pluth "Count: " i)
}
```

## Notes

- All expressions must be enclosed in parentheses when using operators
- Variables must be declared before use
- String indices are 0-based
- The `repeathh` loop counter starts from 0
- Comments are denoted with semicolons (;)
- The `athk` command requires both the prompt and target to be variables:
  - First argument must be a variable containing the prompt string
  - Second argument must be a variable to store the input
