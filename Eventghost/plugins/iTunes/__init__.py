version="0.1.11"

# Plugins/itunes/__init__.py
#
# Copyright (C)  2009 jitterjames  <jitterjames@gmail.com>
#
# This file is part of EventGhost.
#
# EventGhost is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# EventGhost is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EventGhost; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#Last change: 

eg.RegisterPlugin(
    name = "iTunes",
    author = "Stottle, Jitterjames",
    version = version,
    kind = "program",
    createMacrosOnAdd = True,
    description = (
        'Adds support functions to control '
        '<a href="http://www.apple.com/itunes/">iTunes</a>. \n\n<P>'        
    ),
    url = "http://www.eventghost.org/forum/viewtopic.php?f=10&t=1815&start=0",
    icon = (
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEA"
    "mpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iA"
    "lEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKO"
    "g6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEK"
    "JHAAEAizZCFz/SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThL"
    "CIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCR"
    "ACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUp"
    "AAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2"
    "YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+r"
    "cEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ"
    "2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc"
    "5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+"
    "AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQk"
    "LlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiG"
    "zbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggX"
    "mYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGy"
    "UT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAu"
    "xsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKgg"
    "HCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQ"
    "AkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJA"
    "caT4U+IoUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJ"
    "S6WtopXTGmgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3"
    "GK+YTKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XL"
    "VI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGg"
    "sV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H"
    "45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1F"
    "u1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5M"
    "b6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX"
    "4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN"
    "1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l"
    "1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N"
    "/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dn"
    "F2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0"
    "nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5y"
    "n+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7+Hp8"
    "Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGL"
    "w34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6"
    "P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIs"
    "OpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkk"
    "xTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+"
    "xW6Lty8elQfJa7OQrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zv"
    "n//tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0m"
    "ek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3Hjl"
    "G4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7"
    "g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttV"
    "AVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3SPVRSj9Yr60cO"
    "xx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKaRptT"
    "mvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ7"
    "52PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLua"
    "rrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn"
    "7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbr"
    "njg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv"
    "28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMz"
    "LdsAAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADqYAAAOpgAABdvkl/FRgAAC+JJ"
    "REFUeNqUl3mMXfV1xz93fffty7xl3pvNM4PH47HxFmwCtjEIswQMVAkkiLaotE1RaJWl"
    "SkqIqKyKpaFSFeIkhqQNCqEJlBZcKGDAxIZ4wWDAGOOx8Xg8Hs/25r03b9/u8u7tH35O"
    "7Cp/tEf66ScdXZ3z+Z7f+V2dn2DbNhea4zg4joMgCIiCAIIAwBuv7ySbzfLKa6/7R1au"
    "HM5kckFFkaWA11txTH0yGgnOJJNdrF9/JamePgBsx0E4HxcQEfido23CHwKwbQdZlgAo"
    "l/Ps+u3BVbv2Hbp9bDp9Rbyrb5nj2IlLF/eRjEWpmg6VWq1ZXcge89P8qF6tvaK63S/f"
    "cdsWli4Z+r2o/w+AKIoAfHj0+FUP/eTp7x04NnaDL9xJLBZhIBFhsKuDvniIWDiEFooS"
    "6EjQkezAr8F8ucbR3W+fMnTjqVXLhp9YvniwqLlUbMf5vwEI7ZJvf27HD773yL99s1RW"
    "ifRoLF4UoC8WJOjz4gsG8PuDhIIBouEQiWgHqUSCSDKCV4JgO9b0fC4nS9JDkaBvm6oo"
    "/CG7CKCdXP3WP21/8/F/3L4Jf5z+rhV0RmSUUB3J5cZRPWjeIOFQgEgkgN8XIhT00xWL"
    "MDjQSyrqJaXARelarZeQpC8C9v8GkLZu3XqR8q8/9sT+bQ88tp6+JPHuEG7JpN7UyDeh"
    "io0kq2iKildT8KgiEmBbFtVKhZPpIhmXn1SHRuB86xkGTd0YninXrnxi566ZciGvD/X2"
    "VM4DyBee+c+ef+WpH333ocvpGyQYD9NyTNJGBdmU8ZgeRNHAFHR0u07ZKmHX3Ui2ja3r"
    "eIMBCEWIRl3ku0bAcShaNqcaBp8gMa24r3s13HXdT+KRO4F//x3A+a44NTl99b3fevQe"
    "VB+q14VVN6lJEi5FxLELtBpVRCQsoUW91UC0fBiVAv2XDLDh1usIRDuIBwJ0BgO4ZBlL"
    "EDE1ibwPsgbMGxDq6+eNvbv8f5SKg9eL49jIongO4L5HntxGpoi2fDGtuk6t3MQTCiDL"
    "GorSwC3VcEwfRlNCUFrIZotKucSK5BVs3nglFuek1IBRA45acLDhcKRUZaJcgZYNLYvI"
    "bOY7B36z+6krb73FFgQBGeCtdw+t3/X2R5dKS/pxa25KtoiMhdNq4XIE3F4fTcdCsnUc"
    "3U9LMVHUGn1RP16/hx0tOGHDexU4qTsUdBvyC5Cfh1qRPrcL2eVhPD3P3X9+99DBZ/71"
    "G73jJ3/QPTiEjG3xxPO7/hi3n1TCS7FhoGgCHkUER0ASwNBdCLIP3GXqNZ2RcBcb1l9S"
    "TMGJszrBJ3P20mP5DOtTnayZmyCeO8PKzk5ig2FUK8qKSIgDU0W+dvwE7lCQUvfKB5/9"
    "jxd+/J3vPmDK+/btlV5658PN4c4uPF6BaquB5lLRZAlFsHEE0A0B0VFZqFW57rIlzuN/"
    "d/94f39y1KwZ+54dm1vxw4q+VP7Kff9w46aOVQ9se+y20UM6aZdDuLsb0wBZh2JzHgSR"
    "6bF5lqy7JvLyR/u2YNZ3yKMT03HB7euORXwIErhtAZ8ELklAlhwMS0BxO8xlDHqjnWy9"
    "94vz/f3JCtCheNWRFav6kvXDs6wJLx//+x8//bDlW/bqzd/ecv1b702wzOoioYlYpk6l"
    "XgVFI58vEB9McNb0/unH7727Q+ocGBlOix33JcIeWoKCKEDE78bv0dA0DVl1YYkyTUfh"
    "/rtuKKweTJSqTTsQ8AeS6empk8+88Y75Qeei5T3vTx65I3V99nimeTgW06/XvI4/ky4j"
    "izJ2vcLJSoODhsWIpNAfSPLJ2KT2/LaHtsmFaiNpOiGCgQhWTUeVRUIeGZciASJ6y6FZ"
    "NVnZtcjZfOXaifn50/Lw8sHO3+7dd/ima666v/eWL10T/f61X1m9dli4YyC2wrOoszhZ"
    "mN119Ox7d2cXJlEkN4ajU206oGoUynXmp/L4Ip2pvZNzSbneaIg+Xx/eQICG2ABdwu9X"
    "8agSoijQaNmYbpnBrlgrFYt9ZhTSsVKpEP/rv/rq9wdSycyvf/1c69Ln32Gh+XFl3e1/"
    "O4iA4J3zlLe/8xaYs0TCPTiygiEpEIhRSGfIzpxhNld0bb719kvkUn5hxrfERyAcoCko"
    "WIqEP6jiUUQkUURzRBxDJByLSZLfN9HR1ZP+7737Xel6o7l5oJ8utyQmsIlHvUMILAIW"
    "PG5BsiyNUjbLrH8MMdCD43OD4qJSr5GlRcNo4PaHQnJ+8sSZ4NLrqoFQzGc6JWoyeNwy"
    "AbcLzaViImFXW6zuTwmfFCraZF7f89q+g0mxZ/Hao4X8niee+qVx7edu5KsDG7cAVUCc"
    "K9bC43MFPLUmmekxtISXqhOBloPeaFK0DHKZDCtDUkM2K4UFq1Gb9sVSw6oiky0o+L0C"
    "HQEPAbeCLUp0pHz0DnQRdqpf/tqOt17Kfnb6kGPWl1kDIzcXBG1Lp9eDKohlWqZlmEZs"
    "+7/8onf801GWDvrJTn6KO2dSWb4BDBOaDcp1kUap7FSd7KQ8PjnlrK1mD4SS3cOqJmIr"
    "PjxSnUjEQ9jtxh0M0fT5ySlwhdfX/eBVa7be/sPHHhGs2c4Nl39uxcjIpckPdYsPPjhS"
    "r9iZ5tOvvj58aNYI3//o3xDt6ubI2XHGDh2lWS1BfgGhXqFkSsyNfpK97C83TUkA5cy0"
    "uP5PvnHnopgPj8eL7Qj0RIL4OmOIHo3TE59ijB0iP32WtWvW9Pdetm71fHFBUGvpcn/f"
    "kDTT0b+q9P5rhQ9efzM6qns6v/6j7Vy9fBGqJ4gR72c0sYTRRotWZpZ4bpZivkG5OHdk"
    "6z1bfioDSnVuYvf4+2+PbfyLqxenKm6mFpKYioQnDpOjx5E/O4DfF2A+PkizYnPzDZtW"
    "rL1h04rde94rpptW/XiujG8qPZwfnRBXfPNRfD6F3aNZXpwsMjafx9CbGNU6FPM0KhUm"
    "Jwp8Yd3wi+s2XoMERIF8fvq0c+e999zU44JgUKQuwyUKiLkZzJkJmv2X4R9cxiLZoVrV"
    "qVQs5v3d2rNF1X/49ByJ+VOCWD1DbskGRlsJfvnRGKdOzVDLpmlm0pDPIOkVahNTiLrO"
    "jn/+9t0dkY6aBHQA4dLc2ROLVl99/ReGF8U9AnQrEAPibo1jp47xqZwiFuwgV63xwkSe"
    "X53IsPP4FJOnpyB9lnVBLyEjy/FikUNWJ/r4GDTyUC2eW/UqcqOEWNHZtDj2czs7/uze"
    "AwcRgKF2FcqBROrzH83M/GxQunh2/ezoHh78uIrdvZajU9OMpctQrUC9CPUS1HL82Ugf"
    "Htvk0P6XOJ5cSSN1Ka2FHNQqYBqoHhHj8PvcuGpNs3bi7b69+/ZnACRgoA3Qq9cq+cMf"
    "HjHuuevOVRcCRBO9zOSmePzdNPl0CUrzUJyDwjzUynRYRVYnwlSlMOWFOhzbj5mZQmxV"
    "0GQDdyNP/chBlqW66WjM3r9n15tvOeeH0nYF+oEAED87duLU2cyCfNvNNy3+PYLIkOrw"
    "zt6dzExMgl4BqwnNCqRPssrt0NU3RFk3MSUV1R0gUsgRLuhI+TK5M6dZPrCU5Z3aK2/8"
    "13OP6ZZtAq3zAAYQB7qAEKB9/MH7x46fOm1tueWWIUU6N7NZgsqgU8OeO45YnMFdz+Mv"
    "zTKkwtKRVcjhKJpoEVQFopEgrlQfVZLUGgku3/B5BkONN1995qdPVhqWAVQAE3AEQAUS"
    "wDJgCdDT9pX6Fy+55OGHH1l/15e/1AOQA8ZrBoVPT9Kcn6VpGuAL08SmXipRazbJFuuc"
    "ydWYKdbxaSopQTLyJ3a/vvPlF141YRo4BmSBJmBL5yZjnHb8OWABsIBwMb9gvPifz2d3"
    "vrHLtkUp2DM0pMS8Gr3dccJLBgn3DhEKhYj5NVyqRlXQqKNCyyJolWhNfXzmyG9+9dL+"
    "dw++acMEMAoU2upbtAdZkXMPGQ1wtX0uIAJ0cu42RoGlwUBg6RUbN3avv/aGVDCWUmWX"
    "hoCNpTfILxSYmZ1hburMwtRnx87Onhn/JJMv7QFOAPNt1XY7sdkWfdF1E9s9obR3of2x"
    "0/YFLlih9v/De0EF9XYVM+19ASi3qylfEO+i59n/DABeCGc+Nsi5aAAAAABJRU5ErkJg"
    "gg=="
),
)

from win32com.client import Dispatch
from eg.WinApi.Utils import CloseHwnd
import time
import datetime
import wx.lib.masked as masked
from os.path import isfile
import win32com.client
from functools import partial

#====================================================================
class Text:

    Grp1Name = "Simple control of iTunes"
    Grp1Descr = "Basic commands to control iTunes."
    Grp2Name = "More advanced commands."
    Grp2Descr = (
        "Here you find further actions for control of iTunes"
        " (volume, balance, seek) etc.."	
    )
    Grp3Name = "Information Retrieval"
    Grp3Descr = (
        "get settings from iTunes, and information"
        " about current song etc.."
    )
    
    # ITPlaylistSearchFieldAll = 0,
    # ITPlaylistSearchFieldVisible = 1,
    # ITPlaylistSearchFieldArtists = 2,
    # ITPlaylistSearchFieldAlbums = 3,
    # ITPlaylistSearchFieldComposers = 4,
    # ITPlaylistSearchFieldSongNames = 5,
        
    searchTypes = (
      "All",
      "Visible",
      "Artists",
      "Albums",
      "Composers",
      "SongNames"
    )

    
#====================================================================    
#Classes for different types of actions
#====================================================================    

class StdCall(eg.ActionClass):    
    def __call__(self):
        if self.plugin.ComActive():
            try:
                self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.StdCall,self.value))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.StdCall,self.value))

class StartApp(eg.ActionClass):
    def __call__(self):
        if not self.plugin.ComActive():
            self.plugin.StartThread()

class SimpleActions(eg.ActionClass):    
    def __call__(self):
        if self.plugin.ComActive():
            try:
                self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.SimpleActions,self.value))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.SimpleActions,self.value))

            
class ToggleAction(eg.ActionClass):    
    def __call__(self):
        if self.plugin.ComActive():
            try:
                self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.ToggleAction,self.value))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.ToggleAction,self.value))

class SetVolume(eg.ActionClass):
    class text:
        label_tree="Set volume "
        label_conf="Volume Level:"
    def __call__(self, volume):
        if self.plugin.ComActive():
            try:
                self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.SetProperty,self.value,volume))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                print "set volume restarting thread"
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.SetProperty,self.value,volume))
                    
    def GetLabel(self, volume):
        return self.text.label_tree+str(int(volume))+"%"

    def Configure(self, volume=100.0):
        panel = eg.ConfigPanel(self)
        volumeCtrl = eg.SpinNumCtrl(
            panel,
            -1,
            volume,
            max=100.0,
            fractionWidth=1
        )
        panel.AddLabel(self.text.label_conf)
        panel.AddCtrl(volumeCtrl)
        while panel.Affirmed():
            panel.SetResult(volumeCtrl.GetValue())


			
			
			


class ChangeVolume(eg.ActionClass):
    class text:
        label_tree="Change volume by: "
        label_conf="Change by +- %:"
    def __call__(self, volume):
        if self.plugin.ComActive():
            try:
                result=self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.ModifyValue,self.value,volume))                
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                print "set volume restarting thread"
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.ModifyValue,self.value,volume))
            return result
                    
    def GetLabel(self, volume):
        return self.text.label_tree+str(int(volume))+"%"

    def Configure(self, step=0.0):
        panel = eg.ConfigPanel(self)
        volumeCtrl = eg.SpinNumCtrl(
            panel,
            -1,
            step,
            max=100.0,
            min=-100.0,
            fractionWidth=0
        )
        panel.AddLabel(self.text.label_conf)
        panel.AddCtrl(volumeCtrl)
        while panel.Affirmed():
            panel.SetResult(volumeCtrl.GetValue())




class LoadPlaylist(eg.ActionClass):
    class text:
        label_tree="Load Playlist: "
        label_conf="Playlist Name (case sensitive)"
    def __call__(self, plname):
        if self.plugin.ComActive():
            try:
                return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.doLoadPlaylist,plname,self.value))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart\
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.doLoadPlaylist,plname,self.value))
                    
    def GetLabel(self, plname):
        return self.text.label_tree+ plname

    def Configure(self, plname=""):
            panel = eg.ConfigPanel()
            textControl = wx.TextCtrl(panel, -1, plname, style=wx.TE_NOHIDESEL)
            SizerAdd = panel.sizer.Add
            SizerAdd(wx.StaticText(panel, -1, self.text.label_conf))
            SizerAdd(textControl, 0, wx.EXPAND)                    
            
            while panel.Affirmed():
                panel.SetResult(textControl.GetValue())

class SearchAndPlay(eg.ActionClass):
    class text:
        label_tree="Search: "
        label_searchString="Search String: "
        label_searchType="Search Type: "
        label_shuffle = "Shuffle List: "
        playlist = "Playlist Name: "
    def __call__(self, searchType,strSearch, shuffle, playlist="eventghostTemp"):
        if self.plugin.ComActive():
            try:
                self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.doSearchAndPlay,searchType,strSearch,shuffle,playlist))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart\
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.doSearchAndPlay,searchType,strSearch,shuffle,playlist))
                    
    def GetLabel(self, searchType,strSearch, shuffle, playlist="eventghostTemp"):
        return "Search ("+searchType+"): "+strSearch

    def Configure(self, searchType="",searchString="", shuffle=False, playlist="eventghostTemp"):
        panel = eg.ConfigPanel(self)

        isearchTypes = Text.searchTypes       

        try:
            sType = isearchTypes.index(searchType)
        except ValueError:
            sType = 0

        searchTypeCtrl = panel.Choice(sType, isearchTypes)
        searchTextCtrl = panel.TextCtrl(searchString)        
        shuffleCtrl=panel.CheckBox(shuffle)
        playlistCtrl = panel.TextCtrl(playlist)

        panel.AddLine(self.text.label_searchType, searchTypeCtrl)
        panel.AddLine(self.text.label_searchString, searchTextCtrl)        
        panel.AddLine(self.text.label_shuffle,shuffleCtrl)
        panel.AddLine(self.text.playlist, playlistCtrl)

        while panel.Affirmed():
            panel.SetResult(
                isearchTypes[searchTypeCtrl.GetValue()],
                searchTextCtrl.GetValue(),
                shuffleCtrl.GetValue(),
                playlistCtrl.GetValue()
            )
                
class PlaySongInPlaylist(eg.ActionClass):
    class text:
        label_searchString="Song Name: "
        playlist = "Playlist Name: "
    def __call__(self, search, playlist):
        if self.plugin.ComActive():
            try:
                return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.PlaySongInPlaylist,search,playlist))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.PlaySongInPlaylist,search,playlist))
                    
    def GetLabel(self, search, playlist):
        return "Play \""+search+"\" in \""+playlist+"\""

    def Configure(self, search="", playlist=""):
        panel = eg.ConfigPanel(self)
        searchCtrl = panel.TextCtrl(search)    
        playlistCtrl = panel.TextCtrl(playlist)

        panel.AddLine(self.text.label_searchString, searchCtrl)
        panel.AddLine(self.text.playlist, playlistCtrl)

        while panel.Affirmed():
            panel.SetResult(
                searchCtrl.GetValue(),
                playlistCtrl.GetValue()
            )
                
                
class GetTrackInfo(eg.ActionClass):
    def __call__(self):
        if self.plugin.ComActive():
            try:
                #print "I'm trying"				
                return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.GetProperty,self.value))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.GetProperty,self.value))
                
class GetPlaylistInfo(eg.ActionClass):
    def __call__(self):
        if self.plugin.ComActive():
            try:
                #print "I'm trying"				
                return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.GetPlaylistInfo,self.value))
            except:
                #This should mean that the COM server was active, then shutdown and restarted.  
                #The COM instance is from the old thread, so restart
                self.plugin.workerThread.Stop(1)
                self.plugin.workerThread = None
                if self.plugin.ComActive():
                    self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.GetPlaylistInfo,self.value))


class GetUniversal(eg.ActionClass):
    name = "Get Universal"
    description = "Get Universal."
    class text:
        label="Select requested property:"
        get = "Get"
        class Properties:
            Name = "Song Name"
            Album = "Album Name "
            Artist = "Artist Name"
            BitRate = "BitRate"
            BPM = "BPM"
            Comment = "Comment"
            Compilation = "Compilation"
            Composer = "Composer"
            DateAdded = "DateAdded"

    def __init__(self):
        text=self.text
        self.propertiesList=(
            ("Name","Name"),
            ("Album","Album"),
            ("Artist","Artist"),
            ("BitRate","BitRate"),
            ("BPM","BPM"),
            ("Comment","Comment"),
            ("Compilation","Compilation"),
            ("Composer","Composer"),
            ("DateAdded","DateAdded"),			
        )
    def __call__(self, i):
        try:
            return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.GetProperty,self.propertiesList[i][0]))
        except:
            #This should mean that the COM server was active, then shutdown and restarted.  
            #The COM instance is from the old thread, so restart
            self.plugin.workerThread.Stop(1)
            self.plugin.workerThread = None
            if self.plugin.ComActive():
                return self.plugin.workerThread.CallWait(partial(self.plugin.workerThread.GetProperty,self.propertiesList[i][0]))


    def GetLabel(self, i):
        return self.text.get+" "+eval("self.text.Properties."+self.propertiesList[i][1])
#        exec 'from %s import Demo' % demo
    def Configure(self, i=0):
        #text=self.text
        #txt=Text.ListProperties
        choices=[eval("self.text.Properties."+tpl[1]) for tpl in self.propertiesList]
        panel=eg.ConfigPanel(self)
        panel.AddLabel(self.text.label)
        infoCtrl=wx.Choice(
            panel,
            choices=choices,
        )
        infoCtrl.SetSelection(i)
        panel.AddCtrl(infoCtrl)
        while panel.Affirmed():
            panel.SetResult(infoCtrl.GetSelection())




#====================================================================    
#This class is based to the COM object, and responds to events that originate from the COM Server
#====================================================================            

class iTunesEvents():
    def OnPlayerPlayEvent(self, iTrack):
        track = self.comInstance.CurrentTrack
        Payload = {}
        Payload["name"] = track.Name
        Payload["artist"] = track.Artist
        Payload["album"] = track.Album
        Payload["duration"] = track.Duration
        self.plugin.TriggerEvent("TrackChanged",Payload)
    def OnPlayerStopEvent(self, iTrack):
        pass
    def OnAboutToPromptUserToQuitEvent(self):
        #User is trying to close iTunes, close for them to prevent prompt
        eg.PrintNotice("Closing iTunes")
        self.plugin.workerThread.StdCall('Quit')
#====================================================================    
#This class is the thread that hold the COM instance
#====================================================================            
        
class iTunesThreadWorker(eg.ThreadWorker):
    comInstance = None
    plugin = None
    eventHandler = None
    
    def Setup(self, plugin, eventHandler):
        self.plugin = plugin
        self.eventHandler = eventHandler
        try:
            self.comInstance = win32com.client.gencache.EnsureDispatch("iTunes.Application")
            win32com.client.WithEvents(self.comInstance,self.eventHandler)
            self.eventHandler.comInstance = self.comInstance
        except:
            pass
        
    def Finish(self):
        if self.comInstance:
            del self.comInstance
            
    def StdCall(self,value):
        iTunes = self.comInstance
        try:
            getattr(iTunes, value)()
        except:
            # eg.PrintError("invalid iTunes method (%s)"%value)
            eg.PrintNotice("Nothing Playing")

    def SetProperty(self,name,newValue):
        iTunes = self.comInstance
        try:
            setattr(iTunes, name,newValue)
        except:
            eg.PrintNotice("invalid iTunes property (%s)"%name)

    def ModifyValue(self,name,newValue):
        iTunes = self.comInstance
        try:
            i=getattr(iTunes, name)
            setattr(iTunes, name,newValue+i)
            i=getattr(iTunes, name)
            return i
        except:
            eg.PrintError("invalid iTunes property (%s)"%name)

    def doLoadPlaylist(self,PlaylistName, name):
        iTunes = self.comInstance
        try:
            for playlist in iTunes.LibrarySource.Playlists:
                if playlist.Name == PlaylistName:
                    if name == "Play":
                        playlist.PlayFirstTrack()
                    elif name == "Tracks":
                        list = []
                        for track in playlist.Tracks:
                            Payload = {}
                            Payload["Name"] = track.Name
                            Payload["Artist"] = track.Artist
                            Payload["Album"] = track.Album
                            Payload["Duration"] = track.Duration
                            Payload["Enabled"] = track.Enabled
                            list.append(Payload)
                        return list
        except:
            eg.PrintError("Error Loading Playlist")
    
    def PlaySongInPlaylist(self, song, PlaylistName):
        iTunes = self.comInstance
        try:
            for playlist in iTunes.LibrarySource.Playlists:
                if playlist.Name == PlaylistName:
                    for track in playlist.Tracks:
                        if track.Name == song:
                            track.Play()
                            return True
            return False
        except:
            eg.PrintError("Error Loading Playlist")

    def doSearchAndPlay(self,searchType,strSearch,Shuffle, PlaylistName):
        iTunes = self.comInstance
        
        # get the searchtype and convert to integer
        isearchTypes = Text.searchTypes
        try:
            sType = isearchTypes.index(searchType)
        except ValueError:
            sType = 0        
        #print "search type: ",sType
        #print "searching for: ",strSearch
        #print "shuffle: ",Shuffle
        
        #find delete and recreate temp playlist
        try:
            for pl in iTunes.LibrarySource.Playlists:
                if pl.Name == PlaylistName:
                    pl.Delete() 
        except:
            eg.PrintError("Error Clearing Playlist")
        #creating temp playlist
        newPlaylist = iTunes.CreatePlaylist(PlaylistName)
        thePlaylist = win32com.client.CastTo(newPlaylist,'IITUserPlaylist')

        #searching for artist
        if strSearch != "":
            results = iTunes.LibraryPlaylist.Search(strSearch, sType)
            if results == None:
                eg.PrintNotice("Nothing Found")    
            else:            
                for track in results:
                    thePlaylist.AddTrack(track)
                thePlaylist.Shuffle=Shuffle
                thePlaylist.PlayFirstTrack()
        else:
            eg.PrintNotice("Nothing Searched")
    def GetProperty(self,name):
        iTunes = self.comInstance        
        try:
            return getattr(iTunes.CurrentTrack, name)
        except:
            # eg.PrintError("err: invalid iTunes property (%s)"%name)
            eg.PrintNotice("Nothing Playing")
         
    def GetPlaylistInfo(self,name):
        iTunes = self.comInstance
        try:
            if name=="Name":
                return iTunes.CurrentPlaylist.Name
            elif name=="Shuffle":
                return iTunes.CurrentPlaylist.Shuffle
            elif name=="Repeat":
                return iTunes.CurrentPlaylist.SongRepeat
            elif name=="Playlists":
                list = []
                for playlist in iTunes.LibrarySource.Playlists:  
                    list.append(playlist.Name)
                return list
        except:
            return None
    
    def SimpleActions(self,name):
        iTunes = self.comInstance
        
        try:
            if name=="ToggleShuffle":          
              iTunes.CurrentPlaylist.Shuffle = not iTunes.CurrentPlaylist.Shuffle
            elif name=="ShuffleOn":          
              iTunes.CurrentPlaylist.Shuffle = True
            elif name=="ShuffleOff":          
              iTunes.CurrentPlaylist.Shuffle = False
            elif name=="ToggleRepeat":
              if iTunes.CurrentPlaylist.SongRepeat == 0:
                iTunes.CurrentPlaylist.SongRepeat = 2
              elif iTunes.CurrentPlaylist.SongRepeat == 2:
                iTunes.CurrentPlaylist.SongRepeat = 1
              elif iTunes.CurrentPlaylist.SongRepeat == 1:
                iTunes.CurrentPlaylist.SongRepeat = 0
            elif name=="RepeatOff":          
              iTunes.CurrentPlaylist.SongRepeat = 0
            elif name=="RepeatOne":          
              iTunes.CurrentPlaylist.SongRepeat = 1
            elif name=="RepeatAll":          
              iTunes.CurrentPlaylist.SongRepeat = 2
        except:
            eg.PrintNotice("Nothing Playing")
         
    def ToggleAction(self,name):
        iTunes = self.comInstance
        try:
            #toggle the property [getattr(iTunes,name) is the current value]
            setattr(iTunes,name,not getattr(iTunes,name))
        except:
            eg.PrintError("invalid iTunes property (%s)"%name)

#====================================================================    
#This class is the plugin class that EG loads.
#====================================================================            
            
class iTunes(eg.PluginClass):
    workerThread = None
    def __init__(self):
        self.windowMatch = eg.WindowMatcher(u"iTunes.exe",None, None, None, None, 1, False, 0.0, 0)
        group1 = self.AddGroup(Text.Grp1Name,Text.Grp1Descr)
        group1.AddActionsFromList(ACTIONSgrp1)
        group2 = self.AddGroup(Text.Grp2Name,Text.Grp2Descr)
        group2.AddActionsFromList(ACTIONSgrp2)
        group3 = self.AddGroup(Text.Grp3Name,Text.Grp3Descr)
        group3.AddActionsFromList(ACTIONSgrp3)

		

    def StartThread(self):        
        class SubiTunesEvents(iTunesEvents):
            plugin = self
        self.workerThread = iTunesThreadWorker(self, SubiTunesEvents)
        try:
            self.workerThread.Start(20)
        except:
            raise self.Exception("Error starting iTunes worker thread")
    
    def ComActive(self):
        hwnds = self.windowMatch()
        if len(hwnds) != 0:
            if not self.workerThread:
                self.StartThread()
            return True
        elif self.workerThread:
            self.workerThread.Stop(1)
            self.workerThread = None
        eg.PrintNotice("iTunes is not running")
        return False

    def __start__(self):
        self.ComActive()

    def __stop__(self):
        if self.workerThread:
            self.workerThread.Stop(1)
            self.workerThread = None
            
#====================================================================    
#Finally, each line in ACTIONS becomes a new action of the plugin.
#====================================================================            

ACTIONSgrp1 = (
(StartApp, 'StartApp', 'Run iTunes', 'Start iTunes if it is not already running','dummy'),
(StdCall, 'Play', 'Play', 'Play', 'Play'),
(StdCall, 'Stop', 'Stop', 'Stop', 'Stop'),
(StdCall, 'Pause', 'Pause', 'Pause', 'Pause'),
(StdCall, 'Skip', 'Next track', 'Move to next track', 'NextTrack'),
(StdCall, 'Replay', 'Previous track', 'Move to previous track', 'PreviousTrack'),
(StdCall, 'Exit', 'Exit', 'Quit iTunes', 'Quit'),
(StdCall, 'Rewind', 'Rewind', 'Rewind', 'Rewind'),
(StdCall, 'FastForward', 'FastForward', 'Skip forward in a playing track. ', 'FastForward'),
(StdCall, 'Resume', 'Resume', 'Disable fast forward/rewind and resume playback, if playing', 'Resume'),
(ToggleAction, 'VisualsEnabled', 'Toggle Visualization', 'Switch in or out of Visualization mode', 'VisualsEnabled'),
(ToggleAction, 'Fullscreen', 'Toggle Fullscreen', 'Switch in or out of Fullscreen mode', 'FullScreenVisuals'),
(ToggleAction, 'ToggleMute', 'Toggle mute', 'Toggle mute (on/off)', 'Mute'),
(SimpleActions, 'ToggleShuffle', 'Toggle Shuffle', 'Toggle Shuffle (on/off)', 'ToggleShuffle'),
(SimpleActions, 'ShuffleOn', 'Shuffle On', 'Turn Shuffle On', 'ShuffleOn'),
(SimpleActions, 'ShuffleOff', 'Shuffle Off', 'Turn Shuffle Off', 'ShuffleOff'),
(SimpleActions, 'ToggleRepeat', 'Toggle Repeat', 'Toggle Repeat (on/off)', 'ToggleRepeat'),
(SimpleActions, 'RepeatOff', 'Repeat Off', 'Repeat Off', 'RepeatOff'),
(SimpleActions, 'RepeatOne', 'Repeat One', 'Repeat One', 'RepeatOne'),
(SimpleActions, 'RepeatAll', 'Repeat All', 'Repeat All', 'RepeatAll'),
)

ACTIONSgrp2 = (
(SetVolume, 'SetVolume', 'Set Volume Level', 'Sets the volume to a percentage (%).', 'SoundVolume'),
(ChangeVolume, 'ChangeVolume', 'Change Volume Level', 'Modifies the volume by a percentage (%).', 'SoundVolume'),
(LoadPlaylist, 'LoadPlaylist', 'Load Playlist By Name', 'Loads a playlist by name and plays it.', 'Play'),
(SearchAndPlay, 'SearchAndPlay', 'Search n Play', 'Search iTunes for songs and play them.', 'not used'),
(PlaySongInPlaylist, 'PlaySongInPlaylist', 'Play Song In Playlist', 'Play song in specified playlist', 'not used'),
)

ACTIONSgrp3 = (
(GetTrackInfo, 'GetTitle', 'Get Title', 'Returns song title.', 'Name'),
(GetTrackInfo, 'GetAlbum', 'Get Album', 'Returns album name.', 'Album'),
(GetTrackInfo, 'GetArtist', 'Get Artist', 'Returns the artist name.', 'Artist'),
(GetTrackInfo, 'GetGenre', 'Get Genre', 'Returns the genre.', 'Genre'),
(GetUniversal, 'GetUniversal', 'Get Universal', 'Get one of many possible fields for current song.', 'GetUniversal'),
(GetPlaylistInfo, 'GetPlaylistName', 'Get Playlist Name', 'Returns the name of the current playlist', 'Name'),
(GetPlaylistInfo, 'GetPlaylistShuffle', 'Get Playlist Shuffle', 'Returns true or false for shuffle value of the current playlist', 'Shuffle'),
(GetPlaylistInfo, 'GetPlaylistRepeat', 'Get Playlist Repeat', 'Returns 0 for Off, 1 for One Song, or 2 for All Songs', 'Repeat'),
(GetPlaylistInfo, 'GetPlaylists', 'Get Playlists', 'Returns all playlists', 'Playlists'),
(LoadPlaylist, 'GetPlaylistTracks', 'Get Playlist Tracks By Name', 'Loads a playlist by name and return its tracks', 'Tracks'),
)


#this.itunes.CurrentPlaylist.Shuffle = true;