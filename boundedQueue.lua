--[[
Lewis Ellis
KPCB Fellows Application Challenge Question
Implement a bounded queue to store integers using only primitive data types.

I used Lua. I've included comments to explain Lua specifics to make things easier to read.
With Lua installed, you can run this file with "lua boundedQueue.lua"
You can get the Lua source tarball at http://lua.org/ftp

There exists some ambiguity as to whether arrays and such are considered primitive data types.
It almost seems to vary from one language to the next, so I did multiple implementations.
The first uses a string to avoid the primitive ambiguity.
The others use Lua's primitive 'table' type.

This string implementation has:
O(1) enqueue, O(n) dequeue
O(size) space
The O(n) dequeue is based on the gsub replacement; I'm not sure it's actually O(n), but it's certainly more than O(1).
]]

local boundedQueueString = {} --this is our class
boundedQueueString.__index = boundedQueueString --this glues the class to the methods

function boundedQueueString.constructor(s)
  local bq = {} --this is our instance
  setmetatable(bq,boundedQueueString) --this glues the instance to the class

  bq.size = 0
  bq.maxSize = s
  bq.q = ""

  return bq
end

function boundedQueueString:enqueue(n)
  if self.size < self.maxSize then
    self.size = self.size + 1
    self.q = self.q .. n .. "," --append the int and a comma to the string
    return true
  end
  return false
end

function boundedQueueString:dequeue()
  if self.size > 0 then
    self.size = self.size - 1
    local r = self.q:sub(1, self.q:find(",") - 1) --pull the int to return off the front
    self.q = self.q:gsub(r..",", "", 1) --chop off the int that was read
    return r
  end
  return false
end

--[[
This implementation uses a table as an array and has:
O(1) enqueue and dequeue
O(size+d) space where d is the number of dequeues done

Another array implementation can, much like the string implementation, achieve:
O(1) enqueue, O(n) dequeue
O(size) memory
It would simply drop the "start" property and use table.remove in dequeue.
]]

local boundedQueueArray = {}
boundedQueueArray.__index = boundedQueueArray

function boundedQueueArray.constructor(s)
  local bq = {}
  setmetatable(bq,boundedQueueArray)

  bq.size = 0
  bq.maxSize = s
  bq.start = 1 --we have a reading frame which starts at this index
  bq.q = {}
  bq.q[s] = 0 --this gets Lua's VM to allocate memory to the array ahead of time

  return bq
end

function boundedQueueArray:enqueue(n)
  if self.size < self.maxSize then
    self.size = self.size + 1
    self.q[self.start+self.size-1] = n
    return true
  end
  return false
end

function boundedQueueArray:dequeue()
  if self.size > 0 then
    self.size = self.size - 1
    self.start = self.start + 1 --the reading frame slides forward when we dequeue
    return self.q[self.start + self.size]
  end
  return false
end

--[[
These prior implementations make it appear as though there is some kind of tradeoff.
Linked lists can take advantage of pointers to avoid the issue.

This implementation uses tables to construct a linked list structure and has:
O(1) enqueue and dequeue
O(size) memory
Dequeue simply manipulates pointers and lets the garbage collector clean things up
It just detaches the head (O(1)), rather than resetting the value for the entire queue (O(n)) like gsub or table.remove do
]]

local boundedQueueList = {}
boundedQueueList.__index = boundedQueueList

function boundedQueueList.constructor(s)
  local bq = {}
  setmetatable(bq,boundedQueueList)

  bq.size = 0
  bq.maxSize = s
  bq.q = {head = nil, tail = nil}

  return bq
end

function boundedQueueList:enqueue(n)
  if self.size < self.maxSize then
    self.size = self.size + 1

    local newNode = {v = n, next = nil}
    if self.q.tail == nil then
      self.q.head = newNode
    else
      self.q.tail.next = newNode
    end
    self.q.tail = newNode

    return true
  end
  return false
end

function boundedQueueList:dequeue()
  if self.size > 0 then
    self.size = self.size - 1

    local r = self.q.head.v
    self.q.head = self.q.head.next
    if not self.q.head then --or, if self.size == 0
      self.q.tail = nil
    end

    return r
  end
  return false
end


--[[
Test cases using Lua's assert function
assert(e, m) evaluates e to a boolean and if it's false, raises an error with message m
If they all pass, the program's only output should be the last line.
]]

function runTests(size, maxSize, start, tv, hv, hnextv)
  assert(bqs.size == size, "s size")
  assert(bqa.size == size, "a size")
  assert(bql.size == size, "l size")
  assert(bqs.maxSize == maxSize, "s maxSize")
  assert(bqa.maxSize == maxSize, "a maxSize")
  assert(bql.maxSize == maxSize, "l maxSize")
  assert(bqa.start == start, "a start")
  if tv ~= nil then
    assert(bql.q.tail.v == tv, "tail value")
    assert(bql.q.tail.next == nil, "tail next is nil")
  else
    assert(bql.q.tail == nil, "tail nil")
  end
  if hv ~= nil then
    assert(bql.q.head.v == hv, "head value")
    assert(bql.q.head.next.v == hnextv, "head next value")
  else
    assert(bql.q.head == nil, "head nil")
  end
end

bqs = boundedQueueString.constructor(95)
bqa = boundedQueueArray.constructor(95)
bql = boundedQueueList.constructor(95)

for i = 1, 50 do
  bqs:enqueue(i)
  bqa:enqueue(i)
  bql:enqueue(i)
end

runTests(50, 95, 1, 50, 1, 2)

for i = 51, 100 do
  bqs:enqueue(i)
  bqa:enqueue(i)
  bql:enqueue(i)
end

runTests(95, 95, 1, 95, 1, 2)

for i = 1, 90 do
  bqs:dequeue()
  bqa:dequeue()
  bql:dequeue()
end

runTests(5, 95, 91, 95, 91, 92)

for i = 1, 5 do
  bqs:dequeue()
  bqa:dequeue()
  bql:dequeue()
end

runTests(0, 95, 96, nil, nil, nil)

print("Ran to completion")
