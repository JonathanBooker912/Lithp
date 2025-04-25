# Lithp

A Lithp-inthpired programming language with a unique phonetic twitht. Lithp utheth prefix notation and followth a thimple thyntax where expreththionth are enclothed in parenthetheth.

## Inthtallation

```bathh
git clone <repothitory-url>
python lithp.py <filename>
```

## Language Reference

| Conthtruct  | Dethcription            | thyntax Example                      |
| ----------- | ----------------------- | ------------------------------------ |
| `( )`       | Expreththion grouping   | `(pluth 1 2)`                        |
| `thet`      | Variable aththignment   | `thet x 42`                          |
| `dithplay`  | Print to thtdout        | `dithplay "Hello"`                   |
| `athk`      | Read from thtdin        | `athk prompt_var target_var`         |
| `pluth`     | Addition/thtring concat | `(pluth 1 2)` or `(pluth "a" "b")`   |
| `timeth`    | Multiplication          | `(timeth 3 4)`                       |
| `indexth`   | thtring indexing        | `(indexth "hello" 1)`                |
| `repeathh`  | Numeric loop            | `repeathh i 5 { dithplay i }`        |
| `iterateth` | thtring iteration       | `iterateth c "hello" { dithplay c }` |

## Exampleth

### Bathic Arithmetic and thtring Operationth

```lithp
thet a 10
thet b 20
dithplay (pluth a b)
dithplay (timeth a b)
dithplay (pluth "Hello " "World")
```

### thtring Manipulation

```lithp
thet thtr "Lithp"
dithplay (indexth thtr 0)
iterateth c thtr {
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

## Noteth

- All expreththionth mutht be enclothed in parenthetheth when uthing operatorth
- Variableth mutht be declared before uthe
- thtring indiceth are 0-bathed
- The `repeathh` loop counter thtartth from 0
- Commentth are denoted with themicolonth (;)
- The `athk` command requireth both the prompt and target to be variableth:
  - Firtht argument mutht be a variable containing the prompt thtring
  - thecond argument mutht be a variable to thtore the input
