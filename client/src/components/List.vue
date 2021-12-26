<template>
<div>
  <nav class="navbar sticky-top navbar-light bg-light">
    <div class="container-fluid">
      <span class="navbar-brand">MSS Lowest</span>
      <span class="text-end">
        <button v-for="brand,i in brands" :key="i" type="button" class="btn btn-outline-dark mx-1" @click="filterBrand(brand)">{{ brand.ko_name }}</button>
      </span>
    </div>
  </nav>
  <transition name="modal" v-if="modal_open">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
              {{ modal_title }}
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <div v-for="history,i in histories" :key="i">{{ history.created_date }}: {{ history.price }}원</div>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn btn-secondary" type="submit" @click="modal_open=false">닫기</button>
              <a class="btn btn-primary" :href="modal_link" role="button">구매하기</a>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
  
  <div class="container">
    <div class="row">
      <div v-for="product,i in products" :key="i" class="col-sm-4 my-3">
        <div class="card">
          <img :src="product.image" class="card-img-top" :alt="product.name">
          <div class="card-body">
            <h6 class="card-title" style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">{{ product.name }}</h6>
            <ul class="list-group list-group-flush">
              <li class="list-group-item"><button type="button" class="btn btn-info" @click="getHistory(product)">가격 정보 보기</button></li>
            </ul>
          </div>
        </div>    
      </div>
    </div>

    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item">
          <a class="page-link" href="#" @click="goPage(1)" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>

        <li class="page-item" v-for="page_item in page_items" :key="page_item" @click="goPage(page_item)">
          <a v-if="page_item === page_num" class="btn btn-primary" href="#">{{ page_item }}</a>
          <a v-else class="page-link" href="#">{{ page_item }}</a>
        </li>

        <li class="page-item">
          <a class="page-link" href="#" @click="goPage(last_page_num)" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'List',
  data () {
    return {
      brands: '',
      products: '',
      histories: '',
      modal_open: false,
      modal_title: '',
      modal_link: '',
      filter_brand: '',
      page_num: 1,
      last_page_num: 0,
      page_items: [1, 2, 3, 4, 5]
    };
  },
  methods: {
    getBrands() {
      const path = 'http://localhost:8000/api/brands';
      axios.get(path)
        .then((res) => {
          this.brands = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getProducts() {
      const path = `http://localhost:8000/api/products?&page=${this.page_num}&brand=${this.filter_brand}`;
      axios.get(path)
        .then((res) => {
          this.last_page_num = Math.ceil(res.data.count/30);
          this.products = res.data.results;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getHistory(product) {
      const path = `http://localhost:8000/api/history?product=${product.id}`;
      this.modal_title = product.name;
      this.modal_link = product.url;
      this.modal_open = true;

      axios.get(path)
        .then((res) => {
          this.histories = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    filterBrand(brand) {
      this.filter_brand = brand.id;
      this.page_num = 1;
      this.getProducts();
    },
    goPage(page_item) {
      this.page_num = page_item;
      this.page_items = [];
      for (var i=page_item-3; i<=page_item+3; i++) {
        if (i < 1 || i > this.last_page_num) {
          continue;
        }
        else {
          this.page_items.push(i);
        }
      }
      this.getProducts();
    },
    foo(a, b) {
      console.log(a, b)
    }
  },
  created() {
    this.getBrands();
    this.getProducts();
  }
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 400px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
  max-height: 300px;
  overflow-y: auto;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>