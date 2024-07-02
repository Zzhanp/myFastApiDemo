<template>
  <div class="game-purchase-list">
    <el-card>
      <div slot="header">
        <el-input v-model="searchQuery" placeholder="搜索游戏名" @keyup.enter.native="fetchData" style="width: 300px;"></el-input>
        <el-button type="primary" icon="el-icon-search" @click="fetchData">搜索</el-button>
        <el-button type="success" icon="el-icon-plus" @click="openDialog('add')">添加</el-button>
      </div>
      <el-table :data="list" style="width: 100%">
        <el-table-column prop="gameName" label="游戏名" width="180"></el-table-column>
        <el-table-column prop="platform" label="购买平台" width="180"></el-table-column>
        <el-table-column prop="purchaseTime" label="购买时间" width="180"></el-table-column>
        <el-table-column prop="price" label="购买价格" width="180"></el-table-column>
        <el-table-column prop="accountName" label="账户名" width="180"></el-table-column>
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
          <el-date-picker v-model="form.purchaseTime" type="datetime" placeholder="选择日期时间"></el-date-picker>
        </el-form-item>
        <el-form-item label="购买价格">
          <el-input v-model="form.price" type="number"></el-input>
        </el-form-item>
        <el-form-item label="账户名">
          <el-input v-model="form.accountName"></el-input>
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
        purchaseTime: '',
        price: '',
        accountName: ''
      }
    }
  },
  methods: {
    fetchData() {
      getGameList({ search: this.searchQuery }).then(response => {
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
          purchaseTime: '',
          price: '',
          accountName: ''
        }
      }
      this.dialogVisible = true
    },
    handleSave() {
      const api = this.form.id ? updateItem : createItem
      api(this.form).then(() => {
        this.dialogVisible = false
        this.fetchData()
      })
    },
    deleteItem(id) {
      deleteItem(id).then(() => {
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