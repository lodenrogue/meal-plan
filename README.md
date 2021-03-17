Usage:

```sh
python plan.py <calories> <meal-type>
```

Example:
```sh
python plan.py 1586 fish-chicken
```

Available meal types:
- chicken
- fish-chicken

---

Build with Docker:

```sh
docker build -t meal .
```

Run with Docker:

```sh
docker run --rm -it meal 1587 chicken
```
