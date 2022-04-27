SELECT * FROM Customers WHERE City = 'Berlin';

SELECT * FROM Customers WHERE City = 'México D.F.';

SELECT AVG(Price) FROM Products;

SELECT COUNT() FROM Products WHERE Price = 18;

SELECT * FROM Orders WHERE OrderDate BETWEEN '1996-08-01' and '1996-09-06';

SELECT Customers.*, COUNT() AS NumberOfOrders FROM Customers
INNER JOIN Orders ON Orders.CustomerID = Customers.CustomerID
GROUP BY Customers.CustomerID
HAVING NumberOfOrders > 3;

SELECT * FROM Customers
INNER JOIN (SELECT City FROM Customers GROUP BY City HAVING COUNT() > 1) AS Cities
USING (City)
ORDER BY City;