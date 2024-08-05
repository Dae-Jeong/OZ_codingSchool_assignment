from company.BbongCompany import BbongCompany
from person.Person import CEO, StoreOwner, StoreManager, Customer
import datetime


def main():
    ceo = CEO("김CEO", datetime.datetime.now())
    store_owner = StoreOwner("박owner", datetime.datetime.now())
    store_manager = StoreManager("최manager", datetime.datetime.now())
    a_customer = Customer("이customer")

    print(ceo, store_owner, store_manager, a_customer)

    bbong_company = BbongCompany(
        ceo=ceo,
        region="안양",
        founded_dt=datetime.datetime.now()
    )

    seoul_bbong_store = bbong_company.publish_store(
        store_owner=store_owner,
        region="seoul"
    )

    anyang_bbong_store = bbong_company.publish_store(
        store_owner=store_owner,
        region="anyang"
    )
    print(bbong_company, seoul_bbong_store, anyang_bbong_store)

    seoul_bbong_store.sell()
    seoul_bbong_store.change_mode()
    seoul_bbong_store.sell()
    seoul_bbong_store.bbong_selling_system.print_order_list()


if __name__ == '__main__':
    main()
