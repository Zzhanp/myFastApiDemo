<template>
  <div class="game-purchase-list">
    <el-card>
      <el-col class="item-space">
        <el-form label-position="right" :inline="true" ref="form" :model="form" label-width="80px">
          <el-form-item label="游戏名称">
            <el-input v-model="form.gameName" placeholder="请输入游戏名" clearable></el-input>
          </el-form-item>
          <el-form-item label="平台">
            <el-input v-model="form.platform" placeholder="请输入平台" clearable></el-input>
          </el-form-item>
          <el-form-item label="账号">
            <el-input v-model="form.gameAccount" placeholder="请输入账户名" clearable></el-input>
          </el-form-item>
          <el-form-item label="">
            <el-button type="primary" @click="fetchData">查 询</el-button>
          </el-form-item>
          <el-form-item label="">
            <el-button type="primary" @click="handleSave">新 建</el-button>
          </el-form-item>
        </el-form>
      </el-col>
      <el-table :data="list" style="width: 100%">
        <el-table-column prop="gameName" label="游戏名" width="180"></el-table-column>
        <el-table-column prop="platform" label="购买平台" width="180"></el-table-column>
        <el-table-column prop="purchaseDate" label="购买时间" width="180"></el-table-column>
        <el-table-column prop="gamegamePrice" label="购买价格" width="180"></el-table-column>
        <el-table-column prop="gameAccount" label="账户名" width="180"></el-table-column>
        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button size="mini" @click="openDialog('edit', scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="deleteItem(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        @current-change="handlePageChange">
      </el-pagination>
    </el-card>

    <el-dialog :title="dialogTitle" :visible.sync="dialogVisible">
      <el-form :model="form">
        <el-form-item label="游戏名">
          <el-input v-model="form.gameName"></el-input>
        </el-form-item>
        <el-form-item label="购买平台">
          <el-input v-model="form.platform"></el-input>
        </el-form-item>
        <el-form-item label="购买时间">
          <el-date-picker v-model="form.purchaseDate" type="datetime" placeholder="选择日期时间"></el-date-picker>
        </el-form-item>
        <el-form-item label="购买价格">
          <el-input v-model="form.gamePrice" type="number"></el-input>
        </el-form-item>
        <el-form-item label="账户名">
          <el-input v-model="form.gameAccount"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSave">保存</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getGameList, addGame, updateGame, deleteGame } from '@/api/gamePlatform'

export default {
  data() {
    return {
      list: [],
      total: 0,
      searchQuery: '',
      dialogVisible: false,
      dialogTitle: '',
      form: {
        id: '',
        gameName: '',
        platform: '',
        purchaseDate: '',
        gamePrice: '',
        gameAccount: ''
      }
    }
  },
  methods: {
    fetchData() {
      this.pageParams = {
        page: 1,
        per_page: 10
      }
      let params = {
        ...this.pageParams,
        ...this.form
      }
      getGameList(params).then(response => {
        this.list = response.data.items
        this.total = response.data.total
      })
    },
    openDialog(type, row) {
      if (type === 'edit') {
        this.dialogTitle = '编辑游戏购买信息'
        this.form = { ...row }
      } else {
        this.dialogTitle = '添加游戏购买信息'
        this.form = {
          id: '',
          gameName: '',
          platform: '',
          purchaseDate: '',
          gamePrice: '',
          gameAccount: ''
        }
      }
      this.dialogVisible = true
    },
    handleSave() {
      const api = this.form.id ? updateGame() : addGame()
      api(this.form).then(() => {
        this.dialogVisible = false
        this.fetchData()
      })
    },
    deleteItem(id) {
      deleteGame(id).then(() => {
        this.fetchData()
      })
    },
    handlePageChange(page) {
      // 处理分页逻辑
    }
  },
  mounted() {
    this.fetchData()
  }
}
</script>

<style scoped>
.game-purchase-list {
  padding: 20px;
}
</style>