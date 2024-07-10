logo_data = b'''R0lGODdhJgFxAHcAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgAAACwAAAAAJgFxAIcAAAAiIiLExMT///9cXFxGRkZJSUmQkJCTk5PZ2dne3t5ISEj7+/tQUFD4+Pj5+fmbm5vY2Nj39/fi4uIjIyP29vZaWlqRkZH09PT19fWgoKDW1tbz8/Py8vLk5OQmJiYwMDBLS0
vx8fFgYGDw8PDv7++mpqbT09Pt7e3j4+MqKipOTk7r6+vs7OxoaGhra2uXl5d6enrq6uqrq6uJiYk/Pz/Pz8/n5+fo6OguLi7S0tJPT0/l5eXm5uZubm6vr6/h4eHLy8s0NDS1tbXf399zc3OMjIzc3Nzd3d2xsbHHx8fb29va2to6OjpRUVF5eXmLi4vV1dWysrLDw8PU1N
RAQEBSUlLR0dF9fX2KiorOzs60tLQkJCS8vLzMzMzJycnKysqAgICGhobGxsazs7MlJSW3t7dTU1PCwsKCgoKEhITAwMC/v7+wsLC9vb25ubm6urqDg4OBgYEnJydYWFhUVFSqqqorKyukpKSsrKytra1bW1upqamnp6cvLy+dnZ1fX1+ioqKhoaF2dnafn5+enp4oKCiWlp
acnJyZmZmYmJh/f39wcHA4ODiOjo6SkpJiYmJtbW2Pj48+Pj4pKSmHh4eIiIhpaWmFhYVCQkJjY2NHR0d4eHh7e3tycnItLS1qampWVlZNTU1nZ2dmZmZkZGRhYWFeXl5dXV1KSkozMzNXV1dVVVU2NjZMTExDQ0M8PDw9PT1ERERBQUE5OTk7OzsyMjJ+fn6VlZXp6en+/v
6+vr79/f01NTU3NzcxMTH8/PzIyMi7u7uoqKjQ0NC2trZsbGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wADCBxIsKDBgwgTKlxIUMCAhxAjMpyIkEDEiwMoaty4kIDHjyA5ihxJsqRJkQUMnJzoECPElQktunwIs2bBmTRt6tzJk+QBBD0LtpwZNIBMokVN4syYtKnTnQkUOB3qsu
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'''

test_image_wLight_data = b'''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
IoibIojfIo+SEIAAA7'''

test_image_woLight_data = b'''R0lGODdhzgDOAHcAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQECgAAACwAAAAAzgDOAIT///8iIiIwMDAzMjIyMjIlJSUhISEuLi4zMzMxMTE0NDQvLy80MzMmJiYkJCQoJycjIyMxMDA1NDQnJyctLS0hIiIgICA1NTUpKSkAAAAAAAAAAAAAAAAAAAAAAAAAAAAF/yAgjm
RpnmiqrmzrvnAsz3Rt33iu73zv/8CgUBcoGo/I5FEwIDif0KjUWTAor0rDATHtdrHgJNNLhlbDYS23XDah3wkFYk6v2+8Ixfl9NSzkeIF4fGFxgod0elaESX6AiIdujFeGkIKKk0iOloeZSpWcd5ieRZuheJKkRqCniXukpq11qkessqOwf7J2qbS2rbiesbsItKuPu8GZw7
u9qr+nypPMssZF0KHSjNStzqTYnNqE3KfWAeCW4nzkod6e6JDqb+yc5vCI8mj0lu6Z94f50ugiNscesluvhA0k2G/Sv0sJly0kZpBgnojTJjYrUZFgQDD7IHUk9hFLSEQNGf89DFSyj8Zq1lbiaZnlZTeOMQ8Cw7jNZrmcFmk28tkOpzGZoniOI1oPqEel65jyM+pLZzSo86
SKdEoSqz6tKKk+s5rNq0CyoUYmMwsSbCSx39CmY2vSrSC1CBflkjuVBN6dehXy3Xp0MEC6Lg2/9ct1bWCJiu82zkvr5OIRf68+zhg5UOaym3t2RgX33Wg7QjXZ9TwZcOXVpBkXDoq45mk7n8PVHnq7TkpCSFHvVt2bTu65oZcWn/ObTxwG0KNLn06dQeojjqpr125wu/fo14
1k//69ORwGFhkUMGZZ8lH0BNWzh33HhIAE+PPr388/fwMHAAYo4IAEBrgAAf0l2B//AQ9AUOCDD96n4IT6/QfhhQIeSCGFDDqIIYYmDKDAiCSWaOKJIzLggAEstujiizC2GIEEKNaIogQNxKjjjiLa6COJKu4o5Isz/vgjjkMmaYAJBKSHwIrGCLCcAjka02R8TyZHiJRBVU
kLk05CSQuXHnmpypXEoCemKmSSZCYpYGK5JiltJvOmJ2juoqaWfNR5y52ZxJlmllFOCegkecqyZ6Fd8vmGoHoSOqahjqKRaCuLTtqoMZAqKimblFoZZqVh+AnMoYx0iumndIZKy6WnZArqpl+WAGsosrZK65mjMlomqWCoGiurnpgaDaqE3MpJrsW6qoqwuBKbibHZIMuH/7
KWMDuts3Da2qumv4oqJ7BYUBuOtY96O66vbpJ7BbaQaDuJuemgiwa0y0o7L7d4fjtruLWSAC8i8jJCbzz2hjHwIQVvyW+g6g46Z7O7krKwIA33+fAk+Garr8EbM3JxIBm/cTA+CQcbcaQTb1txv+uC2y6nK3va8r4vZzIyHiWjcTJAKWPRcbwfO5wzov7qCvCzNa96M8hHi5
w0xUt3K/DULlcNs8TuKvHzJUFfMTTBRWscdbJY46w1xAIb+WOQlQlAo9s1Imkl3TbCrYoBcuN9Y9hKmFDA4IQXbvjhhS8QgQCMN+7445AzPgHilFdOweKRZx555ZwfrrjmoDs+ef/npF8e+ukmKDlkBQTM7XeJElShuo4WLHDB6yfOviPrruOuQOy6x1j77b6TaB4awdURXi
n04daaZq8th8DxhUw5HHbNz/I8aNFbNH1p/ljfNXHeHxfP9eJlTwf1YCTvyvjYS28+PugzLz37WLg/x/IBtMfabE+BX/ruBz6HiK97FpnfYQRoP+/hjxIH3Jv6CrI93TCwfxP8nmyqQpsL+m8QFUQOAhlSQJVEcC/lC+H5PJjBB37ihIJJIQC7wkICbnAsHRwhRVRIvxo6sI
TAgSFkZMjBAOpwIzeMSw4lKD8eLvCIsnBhEvR3ER8m0IkQsSIJk2iaJaLwijN0DBRvwsX/8HkxhmAsIg3HeAopIoGK/PvgHRSYRTYWpYwGPOMQ04hDIzLxh3g0oR45Q8Q+rvGPFnFjLYRISD4q0Y9f3CJmsMiS+mGwiWGkDCIlKQI6VlKLO8ykazZJjNQFL0YEIF7xYmeBU7
poeMUjkSthlMpY/q4ArZylAWBpSxMcYAHADKYwh0nMYD6gAchMpjKXycxkUqCY0IwmBppJzWr+MprYFOYxq8lNZT4zm+CcZjfHaYI82FIBENCljFTpuws0IJe6NKct06lOA0SAnbhzJzxnOTaGlc1kIUNbzP41s4CNYGd36FmpAnqttEFtbRxr2rCeZjSISm2gSiso066GUa
pp/9RiDq3oRz3RT4z902cMfQNC7aBQMHyNJYBLQklJdtKFnq2hHc3aSNl20JCazaIC5Rq77HTBAMyUZzV1aUot5VOA3jRdHBWqzIgqLqkSlKoGFcFK69DSci1VYU1F6VPvJdFoUfSnO0VaTtWW1lSVNV9ndSpQcWrVjGJ1oz1d60PbGlSWFfWlM4kpEo6a0KR6daxg1atI72
q1vNbVo4zdml+H+qeiEpalhr0CYEUh2CNslQ5d1exXVRbVyU61slU17VVRm1UAfHYOofXaaLHwWgTEVgyzFdtbPRZXsc5VpWG16W/JWlqb/TW3SqjtbZGwWdR01giX5WpmZYtYMCh3uv+4ra7Qdku03gqXr3RVrV1Zi1cReG+5S0BuEs6LXeaqd7BA7FMT2EAGS6qBvmQwxx
jw2wX7boG/XVDkMQYpmkI+8pCRLGV84cDIAjuyi5BEIycB4MmZ2DeDFU4KKJE4SVFCj5S7yLBwNhzFBSOvwcoxMIQRLGEFBzKIBE7xg80Y4T1OWMTKuzAm1ShGEJf4xc5BcVR2bMgeJ5jDnaSkhUncChy/z46cEPA1hJwVIh/YyC1GMoWVrGEoW8LJ+9MxIDvMY00eGSYe5p
6PyUjmIps5y2gu8yjPzOYkp9mCXiaMnD9M5zaauHoxHrKKacxiG7u4zVd+s6FDzOUR5zksQGb/cKCrPOg81riRN250jpn8kzuLcM1+jvSJJ/0VK68Yy4v+MaJPrWhMh3LPau7zHVdNaFS7mtGeXuGjL2NnWOMZ1GnR9JOBHeU/t08B5PFOHP+QbO90p9nVWTayoV0dKZ8DPm
laz67d4wts60nbxO7LCCS0oQlZ6EMX0lC5E9QhdF+I3Ovuz7ndXSB1x3s/7aZ3gUJ0ziDVs0ixRFI9exRLf6sT4KvMUT2jC9r2ple77wquUiEeOO6SzbsTH25iH6vTyPJUqxI/rMatG3LRUlymFvcnxkUOXuAqFq0ej2hxnXbckyPhuis3+ci3O/OJ1nznEX+5XFtOXMeKF7
LkBanQ/31L9DAwHLYON0JzlffcIuD8500nrdGNS9lTFfXqXT+WZVNu0pxTF+jJLfnZs87zrdM87NX6utqzi3aU99ysWI/5RTnOVr0T4um2jXoRpp6IqgcA7Kf1Os3uDte8J12yXE+82Bfvdp/D/VxyX/p3/c4HwKNX6u/17Nzda/MjeF7wASD8/gyP+NUqvrWtH+/reaX5jL
Ndt4znreNnr3S+75XzUK083i9fr8z7frGP/7hrR//wut+c+aAvPXTJTlOz0/32aa89y4FfdK322/rY6VvAWf99D4o/4WMnAenW/7nTgW5067cc5tyfufh3rv30jxz87X840+U/cqakTrxjS//Ao068FEv1ZAADGHCyo0sHWDzWBkdiNmOWVmi3pmq95mZzBmdNJmxhxmmzlo
GJtoGp1oG51kPbFggRSGWlVmmCdGkOlmkn+EThpmcayGccGGq0VoG2FoOvdoOxloMhuGUzWEc1iAhgVkUpGBs7+IIW6IO45mufJmvFJmqABoMyRhBJKG1jJoKsRoIXaIJSqGtHyGtEOIYoWIbcBoS/RoXi5oW11mpQGGdsOIVCWIVNCGNYKGgU6IQ9mIWHBoc8KIeAGIV1SI
ZuCAkrSGpn4YJ6+ISFiIFneIhpmIhI6IFKqIYqaGz5w4KN2IeP+Id8KINoSIOW2AmYyIWJxIkQxIj/bWFqcQiGc1hnkziCOFiCnVaKRniKgrCIe0hpoBhkrlgXNpSHwviLLRiMkoaMnzhhCWgAtcSA+3RKD+g7zxiNq4RLBmg75+RL4ARO2zRO3PRN3yhN4thN11SO0BSO59
hM5KiOxCRO7dhM5XRO6JSA92RL+lRP8hRL9HRw+PQ6+6hOpwd+zYd9SRB7SMd7JEV9SGWQ0ed8oqd9OoeQ8JV73bV7k/cq0Dd4oTd9GHlxGhl3qRV5rreR5bV8FLl23LdxR9dxySdzwtd4xIcwxveSfReTbhWSKjeSmFeSbyd5JAl7HZl6H2l1Ral6eWB4BemTxQeUlieUP0
mUK3l9LUlyw1VJehIJkjOpezWJMjdpkrKHko0Fcll5kFdJW0l5lEblkIUFkR4pfUh5lhFpkabnlpgFl0Ypl4e3lnzZlF8JNGEZlCc5lCmpkDDJkDrjl1tZBIAplU/JkXQZl43ZljxZdk5pk1A5fJCpmVR5fDCnk30llgtJlg15mdWXmWC5mTTZmav5mTj5e6IZXqSZmKapfI
iZk4qpVqA5dGmJeyPAXnqplFRSVMKpmoJJeUOwnMzZnM75nNAZndI5ndRZndZ5ncsZAgA7'''

icon_data = b'''R0lGODdhAAEAAXcAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQECgAAACwAAAAAAAEAAYciIiL////+/v79/f38/Pz7+/v6+vr5+fn4+Pj39/f29vb19fX09PTz8/Py8vLx8fHw8PDv7+/u7u7t7e3s7Ozr6+vq6urp6eno6Ojn5+fm5ubl5eXk5OTj4
+Pi4uLh4eHg4ODf39/e3t7d3d3c3Nzb29va2trZ2dnY2NjX19fW1tbV1dXU1NTT09PS0tLR0dHQ0NDPz8/Ozs7Nzc3MzMzLy8vKysrJycnIyMjHx8fGxsbFxcXExMTDw8PBwcHCwsLAwMC/v7++vr69vb27u7u8vLy6urq5ubm4uLi3t7e2tra1tbW0
tLSzs7OysrKxsbGwsLCvr6+urq6tra2rq6usrKyqqqqpqamoqKinp6empqalpaWkpKSjo6OioqKhoaGgoKCfn5+enp6dnZ2cnJybm5uampqZmZmYmJiXl5eWlpaVlZWUlJSTk5OSkpKRkZGQkJCPj4+Ojo6NjY2MjIyLi4uKioqJiYmIiIiHh4eGhoa
EhISFhYWDg4OCgoKBgYGAgIB/f39+fn59fX18fHx7e3t6enp5eXl4eHh3d3d2dnZ1dXV0dHRzc3NycnJxcXFwcHBvb29tbW1ubm5sbGxra2tqamppaWloaGhnZ2dmZmZlZWVjY2NkZGRiYmJhYWFgYGBfX19eXl5dXV1cXFxbW1taWlpZWVlYWFhXV1
dWVlZVVVVUVFRTU1NSUlJRUVFQUFBPT09OTk5NTU1MTExLS0tKSkpJSUlISEhHR0dGRkZFRUVERERDQ0NCQkJBQUFAQEA/Pz8+Pj49PT08PDw7Ozs6Ojo5OTk4ODg3Nzc2NjY1NTU0NDQzMzMyMjIxMTEjIyMqKiowMDAvLy8uLi4tLS0sLCwnJycrK
yspKSkoKCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABCBxIsKDBgwgTKlzIsKHDhxAj
SpxIsaLFgQEuatzIsaPHjyBDMhQgQKTJkyhTqlyZkGRJljBjypxJc+CAmwRq6tzJs2dEnDd9Ch1KtCaBo0iLKl3K1CPSp02jSp268GgBAlexUt3KNSrWp0m7ih3Ls4ABAwXSqi1Atq1blmfPHjgQ9+zbu3g/0qVrgG/cA3kDC56IYG7huQcKHx7MuHF
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'''