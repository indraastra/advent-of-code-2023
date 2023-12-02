# Solutions

- Days 1: [python](python/Day%201.ipynb)

# Data

```sh
export SESSION="session=..."
curl -b ${SESSION} https://adventofcode.com/2023/day/1/input > day01.txt
```

# Rust

Running:

```sh
cargo run --release --bin day01
```

With logging:

```sh
RUST_LOG=info cargo run --bin day01
```

For benchmarking:

```sh
hyperfine ./target/release/day01
```
