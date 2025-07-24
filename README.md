# Unit Test in Python

Progetto dimostrativo a scopo educativo.

## **Esercizi**

### **Esercizio 1**: Struttura Base

Crea una classe `StringProcessor` con i seguenti metodi:

- `reverse_string(s)`: Inverte una stringa
- `capitalize_words(s)`: Capitalizza ogni parola
- `count_vowels(s)`: Conta le vocali in una stringa

Scrivi i test corrispondenti seguendo le convenzioni di naming.

### **Esercizio 2**: Metodi di Asserzione

Crea una classe `MathOperations` con i seguenti metodi:

- `power(base, exponent)`: Calcola la potenza
- `factorial(n)`: Calcola il fattoriale
- `is_prime(n)`: Verifica se un numero è primo

Scrivi test che utilizzino almeno 8 diversi metodi di asserzione.

### **Esercizio 3**: setUp e tearDown

Crea una classe `TemperatureConverter` che:

- Mantenga una lista di conversioni effettuate
- Abbia metodi `celsius_to_fahrenheit()` e `fahrenheit_to_celsius()`
- Registri ogni conversione con timestamp

Scrivi test che utilizzino setUp/tearDown per:

- Inizializzare il converter
- Verificare che la lista sia vuota all'inizio
- Pulire la lista dopo ogni test

### **Esercizio 5**: Gestione Eccezioni

Crea una classe `PasswordValidator` che:

- Verifica lunghezza minima (8 caratteri)
- Verifica presenza di maiuscole, minuscole e numeri
- Solleva eccezioni personalizzate per ogni tipo di errore

Scrivi test che verifichino tutte le eccezioni possibili.

## Esecuzione dei test

Se **make** è installato:

```bash
make test
```

Se **make** non è installato:

```bash
python -m unittest discover -s test
```
