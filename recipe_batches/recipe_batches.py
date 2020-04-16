#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  if len(ingredients) < len(recipe):
    batches = 0
  else:
    num_batches = {i: ingredients[i] // recipe[i] for i in recipe if i in ingredients}
    cur_val = next(iter(num_batches.values()))
    for j in num_batches:
      if num_batches[j] <= cur_val:
        cur_val = num_batches[j]
        batches = cur_val
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))