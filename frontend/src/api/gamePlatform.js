import request from '@/utils/request'

export function getGameList(params) {
  return request({
    url: '/gamePlatform/list',
    method: 'post',
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

