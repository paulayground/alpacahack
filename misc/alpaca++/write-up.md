# Category

misc

# Overview

Answer the emoji that comes immediately after "🦙" in Unicode code point order, in the flag format.

For example, if that emoji were "🦀", the flag would be Alpaca{🦀}.

# Analysis

🦙의 다음 유니코드를 알기위해 🦙의 유니코드를 확인해 본 결과(`https://symbl.cc/`) `U+1F999`값으로 확인되었다.

# Exploitation

문제에서 제시한 🦙의 다음 값을 알기위해 `U+1F999`에서 1을 더한 `U+1F99A`값을 알 수 있으며, 해당 이모지는 🦚이다.

flag 형식에 맞게 감싸주면 된다.

# Flag

`Alpaca{}`
