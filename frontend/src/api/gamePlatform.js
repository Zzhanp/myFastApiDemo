import request from '@/utils/request'

export function getGameList(params) {
  return request({
    url: '/gamePlatform/list',
    method: 'get',
    params
  })
}

export function addGame(params) {
  return request({
    url: '/gamePlatform/addGame',
    method: 'post',
    params
  })
}

export function deleteGame(params) {
  return request({
    url: '/gamePlatform/deleteById',
    method: 'post',
    params
  })
}

export function updateGame(params) {
  return request({
    url: '/gamePlatform/updateById',
    method: 'post',
    params
  })
}

