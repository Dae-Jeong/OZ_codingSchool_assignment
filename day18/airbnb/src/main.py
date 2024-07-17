from src.db import DBManager


def main():
    db_manager = DBManager()

    # 새로운 제품 추가
    query_1 = "insert into Products (productName, price, stockQuantity) values (%s, %s, %s)"
    values = ("Python book", 29.99, 0)
    db_manager.insert_data(query=query_1, params=values)

    # 고객 목록 조회
    query_2 = "select * from Customers"
    result_1 = db_manager.execute_query(query=query_2);
    print(f'고객 정보 -> {result_1}')
    print()

    # 제품 재고 업데이트
    # 제품 : Maintain Whole 구매 / 개수 : 3개
    query_3 = "select * from Products where productID = 6"
    result_2 = db_manager.execute_query(query=query_3)

    original_quantity = result_2[0].get('stockQuantity')
    purchase_quantity = 3

    calculated_quantity = original_quantity - purchase_quantity
    if calculated_quantity < 0:
        raise ValueError("재고보다 많은 양을 구매할 수 없습니다.")

    query_4 = "update Products set stockQuantity=%s where productID = 6"
    value_2 = (calculated_quantity, )
    db_manager.update_data(query=query_4, params=value_2)

    # 고객별 총 주문 금액 계산
    query_5 = "select customerId, SUM(totalAmount) from Orders group by customerId"
    result_3 = db_manager.execute_query(query=query_5)
    print(result_3)
    print()

    # 고객 이메일 업데이트
    # 이메일 : helloworld@gmail.com, customerID : 4
    query_6 = "update Customers set email = %s where customerID = %s"
    value_3 = ("helloworld@gmail.com", 4)
    db_manager.update_data(query=query_6, params=value_3)

    # 주문 취소
    query_7 = "delete from Orders where orderID = %s"
    value_4 = (15, )
    db_manager.delete_data(query=query_7, params=value_4)

    # 특징 제품 검색
    query_8 = "select * from Products where productName like %s"
    value_5 = ("%Book%",)
    result_4 = db_manager.execute_query(query=query_8, params=value_5)
    print(result_4)
    print()

    # 특정 고객의 모든 주문 조회
    query_9 = "select * from Orders where customerID = %s"
    value_6 = (3, )
    result_5 = db_manager.execute_query(query=query_9, params=value_6)
    print(result_5)
    print()

    # 가장 많이 주문한 고객 찾기
    query_10 = ("select customerId, count(*) as orderCount from Orders "
                "group by customerId "
                "order by orderCount desc "
                "limit 1")
    result_6 = db_manager.execute_query(query=query_10)
    print(result_6)
    print()

    db_manager.close_connection()


if __name__ == "__main__":
    main()
