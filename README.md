# Pollen Python Api

This provides a simple python library to obtain the current pollen count for a specified location from [Benadryl's Social Pollen Count](https://benadryl.co.uk/social-pollen-count/).

Note: The Benadryl Social Pollen Count service only covers the United Kingdom.

## Installation

```bash
pip install pypollen
```

## API

### Constructor

`location` can be a UK postcode or city.
#FIXME

```python
Pollen(latitude,longitude)
```

### Properties

```python
pollencount # String with level of pollen
```

## Example

```python
from pollen import Pollen

print Pollen(51.7546407,-1.2510746).pollencount
```
