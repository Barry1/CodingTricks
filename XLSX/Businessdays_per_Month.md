# Businessdays per month

Sometimes - for example related to taxes - you need to quickly find out, how many working days are there within a given month.
This task can easily be solved with excel. In the following lines I assume working days are from Monday to Friday.

## quick readers solution

Okay, for those, who just want a formula: Insert the month of interest (as date) within a cell - for the formula we assume `A1`.
Then enter the formula

```excel
=(TAG(DATUM(JAHR(A1);MONAT(A1)+1;1)-1)-WOCHENTAG(DATUM(JAHR(A1);MONAT(A1)+1;1)-1)-(8-WOCHENTAG(DATUM(JAHR(A1);MONAT(A1);1))))/7*5+MIN(5;7-WOCHENTAG(DATUM(JAHR(A1);MONAT(A1);1)))+MIN(5;WOCHENTAG(DATUM(JAHR(A1);MONAT(A1)+1;1)-1)-1)
```

into you cell of interest - and here we are - you can see the number of business days. Public holidays are not taken into account.

## now with explanantion

As we do not know, if the first and/or last week is incomplete, we count in three different steps.

### the first week in the month

### the last week in the month

### the weeks in between
