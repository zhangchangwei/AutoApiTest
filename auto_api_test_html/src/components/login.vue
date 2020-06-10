<style lang="less" scoped>
.div-a {
  position: absolute;
  left: 38%;
  top: 30%;
  width: 450px;
  height: 200px;
}
.div-a /deep/ .ivu-card{
  background: #a6dede7d;;
}
</style>

<template>
  <div id="band" >
    <div class="div-a">
      <Card>
        <Tabs value="custom" style="max-height: 300px;">
          <TabPane label="普通登录" name="custom">
            <Form ref="formInline" :model="formInline" inline>
              <Form-item prop="user" style="width: 100%">
                <Input prefix="md-person" v-model="formInline.user" placeholder="Username" autofocus />
              </Form-item>
              <Form-item prop="password" style="width: 100%">
                <Input prefix="ios-lock-outline" type="password" v-model="formInline.password" placeholder="Password" />
              </Form-item>
              <!-- <Form-item>
                <Input type="text" placeholder="请输入验证码" v-model="identifyCodetxt" @on-keydown="enterToSelect" />
              </Form-item>
              <div class="code" @click="refreshCode">
                <SIdentify :identifyCode="identifyCode"></SIdentify>
              </div> -->

              <Form-item style="width: 100%">
                <Button type="primary" style="width: 100%" size="large">登录</Button>
              </Form-item>
            </Form>
          </TabPane>
        </Tabs>
      </Card>
    </div>
  </div>
</template>
<script>

export default {
  name: 'Login',
  components: {
  },
  data () {
    return {
      formInline: {
        user: '',
        password: ''
      }
    }
  },
  created: function () {
  },
  methods: {
  },
  mounted () {
    window.particlesJS.load(
      'band',
      '/static/particlesjs-config.json'
    )
  }
}
</script>
