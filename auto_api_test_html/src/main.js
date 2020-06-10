
import Vue from 'vue'

import iView from 'view-design'
import 'view-design/dist/styles/iview.css'
import particles from 'particles.js/particles'//  实现登陆页粒子

import Subnet from './subnet.vue'
import router from './router'

import config from './libs/util'

Vue.use(iView)
Vue.use(particles)
Vue.config.productionTip = false
Vue.prototype.$config = config

/* eslint-disable no-new */
new Vue({
  el: '#Subnet',
  template: '<Subnet/>',
  components: { Subnet },
  // store: store,
  router: router
})
