const { createApp } = VuecreateApp({    delimiters: ['${', '}$'],    mixins: [window.mix ? window.mix : {}],    methods: {        postData(url, payload, config) {            return axios.post(url, payload, config ? config : {})                .then(response => {                    return response.data ? response.data : response.json?.()                }).catch(() => {                    console.warn('Метод ' + url + ' не реализован')                    throw new Error('no "post" method')                })        },        getData(url, payload) {            return axios.get(url, { params: payload })                .then(response => {                    return response.data ? response.data : response.json?.()                })                .catch(() => {                    console.warn('Метод ' + url + ' не реализован')                    throw new Error('no "get" method')                })        },        search() {            location.assign(`/catalog?filter=${this.searchText}`)        },        getCategories() {            this.getData('/api/categories')                .then(data => this.categories = data)                .catch(() => {                    console.warn('Ошибка получения категорий')                    this.categories = []                })        },        getBasket() {            const basket = {}            this.getData('/api/basket')                .then(data => {                    data.forEach(item => {                        basket[item.id] = {                            ...item                        }                    })                    this.basket = basket                }).catch(() => {                    console.warn('Ошибка при получении корзины')                    this.basket = {}                })        },        getLastOrder() {            this.getData('/api/orders/active').then(data => {                this.order = {                    ...this.order,                    ...data                }            }).catch(() => {                console.warn('Ошибка при получении активного заказа')                this.order = {                    ...this.order,                }            })        },        addToBasket (item, count) {            const id = item.id            this.postData('/api/backet/', {                headers: { "X-CSRFToken": '{{csrf_token}}' },                id: item.id,                some: 'its',                count: count || 1            }).then(data => {                this.basket[id] = data            }).catch(() => {                console.warn('Ошибка при добавлении заказа в корзину')            })        },        removeFromBasket(item, count) {            const id = item.id            axios.delete('/api/basket', { params: { id, count } })                .then(response => response.json())                .then(data => { // updated basket                    this.basket = data                }).catch(() => {                    console.warn('Ошибка при удалении заказа из корзины')                })        }    },    computed: {        basketCount () {            return (this.basket && Object.values(this.basket)?.reduce((acc, val) => {                acc.count += val.count                acc.price += val.price                return acc            }, { count: 0, price: 0 })) ?? { count: 0, price: 0 }        }    },    data() {        return {            // catalog page            filters: {                price: {                    minValue: 1,                    maxValue: 50000,                    currentFromValue: 7,                    currentToValue: 27,                },            },            sortRules: [                { id: 'rating', title: 'Популярности'},                { id: 'price', title: 'Цене'},                { id: 'reviews', title: 'Отзывам'},                { id: 'date', title: 'Новизне'},            ],            topTags: [            ],            // reused data            categories: [],            categoriesFromServer: [            ],            // reused data            catalogFromServer: [            ],            orders: [],            cart: [],            paymentData: {},            basket: {},            order: {                orderId: null,                createdAt: '',                products: [],                fullName: '',                phone: '',                email: '',                deliveryType: '',                city: '',                address: '',                paymentType: '',                totalCost: 0,                status: ''            },            searchText: ''        }    },    mounted() {        this.getCategories()        this.getBasket()        this.getLastOrder()    }}).mount('#site')