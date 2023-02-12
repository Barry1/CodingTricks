# Businessdays per month

Sometimes - for example related to taxes - you need to quickly find out, how many working days are there within a given month.
This task can easily be solved with excel. In the following lines I assume working days are from Monday to Friday.

## quick readers solution

Okay, for those, who just want a formula: Insert the month of interest (as date) within a cell - for the formula we assume `A1`.
Then enter the formula

```excel
=
 MIN(5,7-WEEKDAY(DATE(YEAR(A1),MONTH(A1),1)))
 +MIN(5,WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)-1)
 +(
     DAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)
     -(8-WEEKDAY(DATE(YEAR(A1),MONTH(A1),1)))
     -WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)
  )/7*5
```

into you cell of interest - and here we are - you can see the number of business days. Public holidays are not taken into account.

## With explanantion

As we do not know, if the first and/or last week is incomplete, we count in three different steps.

### the first week in the month

First we calculate the weekday of the first day within the month of interest by `WEEKDAY(DATE(YEAR(A1),MONTH(A1),1)`.
To find out, how many working days are in the first month, we simply subtract from seven but cap to 5:

```excel
MIN(5,7-WEEKDAY(DATE(YEAR(A1),MONTH(A1),1)))
```

### the last week in the month

First we calculate the weekday of the las day within the month of interest by `WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)`. (This is of course one day before the first of the next month.)
To find out, how many working days are in the last month, we just cap the predecessors value to 5:

```excel
MIN(5,WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)-1)
```

### the weeks in between

This might be last easiest step: For each week in between (excluding) the first and the last week, we have 5 working days per those 7 days of the weeks.
How to get the number of in between days?
Just start with the last day number of the month `DAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)` and now subtract the number of days in the first week `8-WEEKDAY(DATE(YEAR(A1),MONTH(A1),1))` and the numbers of days in the last week `WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)`.
Scaling with `5/7` now leads to the wanted

```excel
(
     DAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)
     -(8-WEEKDAY(DATE(YEAR(A1),MONTH(A1),1)))
     -WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1)-1)
)/7*5
```

## Example

![Example-image](https://user-images.githubusercontent.com/230051/139531275-9086766c-fafe-42d5-a7dc-7ebf3073af16.png)
